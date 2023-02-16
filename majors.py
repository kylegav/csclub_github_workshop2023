class Major:
    def __init__(self, department_id: int, name: str, division: str):
        self.department_id = department_id
        self.name = name
        self.division = division

    def __str__(self):
        return f"Department ID: {self.department_id}\nDepartment Name: {self.name}\nDivision of: {self.division}" \
               f"\n =============================="
