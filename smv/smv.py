import os
import paramiko


class SMVClient(object):
    #use status variables so you can query the status on the fly (progress etc)

    def __init__(self, remotehost, remoteuser, localpath=".", port=22):
        self.localpath = localpath
        self.ssh = paramiko.SSHClient()
        #self.ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        self.ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect(remotehost, port=port, username=remoteuser)
        self.sftp = self.ssh.open_sftp()

    def get(self, remotepath):
        #get items from remote path and place them in local path return list of items got
        stuff = self.sftp.listdir(remotepath)
        return stuff

    def delete(self, items):
        #delete items return list of deleted items
        return items

    def check_file(self, file1, file2):
        #placeholder for now this should do a checksum
        return file1 == file2

    def _close(self):
        self.ssh.close()

    def run(self, remotepaths):
        for remotepath in remotepaths:
            items_to_delete = self.get(remotepath)
            print items_to_delete
            items_deleted = self.delete(items_to_delete)
            print items_deleted
            if items_to_delete != items_deleted:
                print "Error {0}".format(items_to_delete-items_deleted)

if __name__ == '__main__':
    smv = SMV("beerus.rahulmohandas.com", "rahul")
    dirs = ["/home/rahul/"]
    smv.run(dirs)
    #smv = SMV("beerus.rahulmohandas.com:/home/rahul/unpack/scene", "/tmp", port=22)


#sftp = ssh.open_sftp()
#sftp.put(localpath, remotepath)
#sftp.close()
#ssh.close()
