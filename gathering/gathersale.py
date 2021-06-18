from datetime import datetime
#import time

import cupang
import bamin
#import naver
import yogiyo

if __name__ == '__main__':
    
    total = 0

    d = datetime.now()
    dt_string = d.strftime('%Y/%m/%d\t%H:%M')
    with open("/home/pi/workspace/gathering/gather_data.cvs", "a") as f:
        f.write(dt_string)
#        time.sleep(2)

    # bamin_gather()
    배민바로결제, 배민만나서결제 = bamin.bamin_gather()
    total = total + int(배민바로결제.replace(',',''))
    total = total + int(배민만나서결제.replace(',',''))
    with open("/home/pi/workspace/gathering/gather_data.cvs", "a") as f:
        f.write('\t' + 배민바로결제 + '\t' + 배민만나서결제)
#        time.sleep(2)

    #cupang_gather()
    쿠팡결제 = cupang.cupang_gather()
    total = total + int(쿠팡결제.replace(',',''))
    with open("/home/pi/workspace/gathering/gather_data.cvs", "a") as f:
        f.write('\t' + 쿠팡결제)
#        time.sleep(2)

    #yogiyo_gather()
    요기요온라인결제, 요기요만나서결제 = yogiyo.yogiyo_gather()
    total = total + int(요기요온라인결제.replace(',',''))
    total = total + int(요기요만나서결제.replace(',',''))
    with open("/home/pi/workspace/gathering/gather_data.cvs", "a") as f:
        f.write('\t' + 요기요온라인결제 + '\t' + 요기요만나서결제)
#        time.sleep(2)

#    sum_naver = naver.naver_gather()
#    total = total + int(sum_naver.replace(',',''))
#    with open("gather_data.cvs", "a") as f:
#        f.write('\t' + sum_naver)
#        time.sleep(2)

    with open("/home/pi/workspace/gathering/gather_data.cvs", "a") as f:
        f.write('\t' + str(total))
#        time.sleep(2)
    with open("/home/pi/workspace/gathering/gather_data.cvs", "a") as f:
        f.write('\n')