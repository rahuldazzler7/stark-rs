from common.system_analyser.system_info import System_Information, CPU_usage, last_boot, Virtual_memory, Swap_memory, \
    Disk_info, read_write_stats_of_disk
from flask_restful import Resource, reqparse
from common.flask_ease.request_validation import validate_request


class System_info(Resource):
    def post(self):
        si = System_Information()
        verify = validate_request("type")
        details_args = reqparse.RequestParser()
        det = details_args.parse_args()
        if det["type"] is "os":
            os = si.operating_sys()
            return {"status": True, "type": "system_info", "data": f"{os}"}
        else:
            all = si.all_info()
            return {"status": True, "tune": False, "type": "system_info", "data": f"{all}"}


class CPU_info(Resource):
    def post(self):
        ci = CPU_usage()
        cpu_result = ci.all_info()
        return {"status": True, "tune": False, "type": "cpu_info", "data": f"{cpu_result}"}


class Last_boot_info(Resource):
    def post(self):
        lb = last_boot()
        return {"status": True, "tune": True, "type": "last_boot_info", "data": f"{lb}"}


class Disk_info(Resource):
    def post(self):
        di = Disk_info()
        disk_details = di.partitiones_usage_info()
        return {"status": True, "tune": False,  "type": "disk_info", "data": f"{disk_details}"}


class Memory_info(Resource):
    def post(self):
        vm = Virtual_memory()
        sm = Swap_memory()
        verify = validate_request("query")
        if verify:
            if verify["query"] is "vm" or "virtual" in verify["query"]:
                virtual_m = vm.all_info()
                return {"status": True, "tune": False,  "type": "memory_info", "data": virtual_m}
            elif verify["query"] is "sm" or "swap" in verify["query"]:
                swap_m = sm.all_info()
                return {"status": True, "tune": False, "type": "memory_info", "data": swap_m}
            else:
                virtual_m = vm.all_info()
                swap_m = sm.all_info()
                memory_arr = [virtual_m, swap_m]
                return {"status": True, "tune": False, "type": "memory_info", "data": memory_arr}
