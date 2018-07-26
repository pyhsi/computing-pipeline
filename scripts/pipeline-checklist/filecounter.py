import os
import sys
from datetime import date, timedelta

stereotop_dir = '/data/terraref/sites/ua-mac/raw_data/stereoTop/'
rgb_geotiff_dir = '/data/terraref/sites/ua-mac/Level_1/rgb_geotiff/'
flir_ir_dir = '/data/terraref/sites/ua-mac/raw_data/flirIrCamera/'
ir_geotiff_dir = '/terraref/sites/ua-mac/Level_1/ir_geotiff/'


def get_counts_for_date(date_string):
    result = date_string

    current_stereotop_dir = stereotop_dir+date_string
    current_rgb_geotiff_dir = rgb_geotiff_dir + date_string
    current_flir_ir_dir = flir_ir_dir + date_string
    current_ir_geotiff_dir = ir_geotiff_dir + date_string

    stereotop_count = len(os.listdir(current_stereotop_dir))
    result += ','
    result += stereotop_count
    rgb_geotiff_count = len(os.listdir(current_rgb_geotiff_dir))
    result += ','
    result += str(rgb_geotiff_count)
    flir_ir_count = len(os.listdir(current_flir_ir_dir))
    result += ','
    result += str(flir_ir_count)
    ir_geotiff_count = len(os.listdir(current_ir_geotiff_dir))
    result += ','
    result += str(ir_geotiff_count)
    return result


def main():
    command_line_arguments = sys.argv[1:]
    if len(command_line_arguments) == 1:
        print('just one date')
        date_string = sys.argv[1]
        date_string = date_string.split('-')
        current_date = date(int(date_string[0]), int(date_string[1]), int(date_string[2]))
        print(current_date)
    else:
        start_date_string = sys.argv[1]
        start_date_string = start_date_string.split('-')
        start_date = date(int(start_date_string[0]), int(start_date_string[1]), int(start_date_string[2]))
        #print(start_date)
        end_date_string = sys.argv[2]
        end_date_string = end_date_string.split('-')
        end_date = date(int(end_date_string[0]), int(end_date_string[1]), int(end_date_string[2]))
        delta = end_date - start_date
        for i in range(delta.days + 1):
            print(start_date + timedelta(i))

    print(command_line_arguments)

if __name__ == '__main__':
    main()