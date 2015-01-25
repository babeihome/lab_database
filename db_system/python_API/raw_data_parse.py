__author__ = 'beibeihome'
import config
import friendly_api
import MySQLdb

def import_data():
    """
    print 'Please input user'
    USER = raw_input()
    print 'Please input passwd'
    PASSWD = raw_input()
    print 'Please input file needed import'
    PATH = raw_input()
    if PATH == '':
        PATH = './PedestalPar'
    """
    PATH = '/data/beamTest/2nd_2014_10/Calibration/DAMPE/Pedestal/PedestalPar'
    fp = open(PATH)

    # file kind judgement
    file_type = 'EXPERIMENT'

    para_list = {}
    if file_type == 'EXPERIMENT':
        # This data file has a constraint form. First line is the name of experiment , second line is start time, and third
        # line is end time.
        E_name = fp.readline().rstrip('\n')
        para_list['E_time0'] = fp.readline().rstrip('\n')
        para_list['E_time1'] = fp.readline().rstrip('\n')
        para_list['data_package'] = fp.read()

    elif file_type == 'SET':
        # have not been finished
        pass
    else:
        print 'File is not in right form'

    conn = MySQLdb.connect(host=config.HOST, user=config.USER, passwd=config.PASSWD, db=config.DATABASE, port=config.PORT)
    if file_type == 'EXPERIMENT':
        friendly_api.InsertData(conn, 'exp_data', para_list)

        # auto update time_index
        time_index = {}
        order = 'SELECT S_time FROM set_data WHERE S_time <= ' + para_list['E_time0'] + ' ORDER BY S_time DESC LIMIT 1'
        cur = conn.cursor()
        cur.execute(order)
        result = cur.fetchone()
        time_index['S_time'] = str(result[0])
        time_index['E_time0'] = para_list['E_time0']
        time_index['E_name'] = E_name
        friendly_api.InsertData(conn, 'time_index', time_index)










