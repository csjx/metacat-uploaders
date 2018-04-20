#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright 2018 The Regents of the University of California
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""SFTP Uploader
    This uploader assumes that files to be uploaded and registered in Metacat are physically on another system, and that the SFTP protocol is available for connections on the Metacat server.
    
"""

import os
import logging
import io
import time
import sys
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import d1_client
import postgresql
import pandas as pd
from random import randint
import paramiko

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

class SFTPUploader:
    
    def __init__(self, object_list_path):
        """Constructor - initialize the SFTPUplodaer instance.
        """
        self.object_list_path = object_list_path
        self.object_list = pd.read_csv(self.object_list_path, delimiter=",")
        self.source_host = "datateam.nceas.ucsb.edu"
        self.source_port = 22
        self.username = "<your-ssh-username>"
        self.password = "<your-password>"
        self.destination_dir = os.path.join(os.sep, "home", "cjones", "mayer")
    
    def _upload(self, row):
        """Upload a data file to the Metacat storage directory via SFTP.
        """
        try:
            # Delay each upload to avoid server saturation exceptions
            delay = randint(1,20)
            log.info("Sleeping " + str(delay) + " seconds before connecting.")
            time.sleep(delay)
            # Establish an SFTP client 
            transport = paramiko.Transport(self.source_host, self.source_port)
            transport.connect(username = self.username, password = self.password)
            sftpClient = paramiko.SFTPClient.from_transport(transport)
            # Get the file
            r = sftpClient.get(row[1].filepath, os.path.join(self.destination_dir, row[1].pid))
        
        except paramiko.ssh_exception.SSHException as ssh_exception:
            log.info("Failed: " + ssh_exception)
            raise
        
        finally:
            sftp.close()
            transport.close()
        
        return row
        
    def _register(self):
        """Register a data file into the Metacat PostgreSQL database.
        """
        
    def run(self):
        """Run the uploader and schedule upload tasks.
        
        Use the default number of concurrent threads for the Executor (5 per core).
        """
        start = time.time()
        
        with ThreadPoolExecutor(max_workers = 16) as executor:
            futures = [executor.submit(self._upload, row) for row in self.object_list.iterrows()]
            concurrent.futures.wait(futures)
            
            # for result in executor.map(self._upload, self.object_list.iterrows()):
            #     log.info("Record: {0}, pid: {1}".format(result[0], result[1].pid))
            
        log.info('time: {0}'.format(time.time() - start))
        
def main():
    object_list_path = os.path.join(os.sep, "Users", "cjones", "mayer2014.csv")
    uploader = SFTPUploader(object_list_path);
    uploader.run()
    
if __name__ == '__main__':
    main()

