from service import readExcel
from service import actualsService
from util import dbUtils as db
from service import actualsDao

def main():
    readExcel.upload_data()
    # actualsService.process_actuals()

if __name__ == "__main__":
    main()