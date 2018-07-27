import csv


class FileHandle:
    __instance = None

    @classmethod
    def getinstance(cls):
        # print('#3', cls)
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        # print('#1', cls(*args, **kargs))
        cls.__instance = cls(*args, **kwargs)
        # print('#2', cls.__instance)
        cls.instance = cls.getinstance
        return cls.__instance

    def file_reader(self, file_name, read_select_type, encoding):
        r = open(file_name, read_select_type, encoding=encoding)
        rs = list(csv.reader(r))
        r.close()
        return rs

    def file_writer(self, file_name, read_select_type, encoding, obj, max_id_value):
        f = open(file_name, read_select_type, encoding=encoding, newline='')
        wr = csv.writer(f)
        wr.writerow([
            max_id_value + 1,
            obj.customer.__dict__,
            obj.room.__dict__,
            obj.fr_date,
            obj.to_date
        ])
        f.close()

    def file_reader_get_max_id(self, file_name, read_select_type, encoding):
        rs = self.file_reader(file_name, read_select_type, encoding)
        max_id_value = 0
        for i in rs:
            if int(i[0]) > max_id_value:
                max_id_value = int(i[0])
        return max_id_value
