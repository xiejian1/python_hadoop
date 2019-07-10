from hdfs import Client

class HDFSData():
    """查看hdfs下面的文件和目录"""

    def conn(self):
        client = Client('http://192.168.0.107:11070')

        return client

    def get_dir(self):

        client = self.conn()

        dirs = client.list('/analys')

        for dir in dirs:
            print("文件的路径",dir)

    def make_dir(self):
        """创建目录"""
        client = self.conn()

        client.makedirs('/analys/mysql/')



if __name__ == "__main__":
    hdfs = HDFSData()

    hdfs.get_dir()