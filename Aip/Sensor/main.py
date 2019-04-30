from Sensor import yysb as yysb, test as record
import  time

if __name__ == '__main__':
        while True:
                record.recording()
                time.sleep(1)
                yysb.AipTest()
                time.sleep(1)