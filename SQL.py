def sql_generate(table: str, columns=[], **kwargs):
    sql_str = ""
    # test table argument is string type
    if not isinstance(table, str):
        raise ValueError("table should be a string which named a table.")

    # select all columns (a *) if columns argument is a empty list
    if len(columns) == 0:
        columns = ["*"]

    # add table and columns to generated sql query string
    sql_str = f"SELECT {', '.join(columns)}\nFROM {table}"

    # add filter to generated sql query string
    if "where" in kwargs and "whereArg" in kwargs:
        # where and whereArg both in kwargs

        # test where argument should be a string
        if not isinstance(kwargs["where"], str):
            raise ValueError("where should be a string.")
        # test whereArg argument should be a string
        if not isinstance(kwargs["whereArg"], list):
            raise ValueError("whereArg should be a list which contains argument for where template string")
        # generate where and whereArg to query string
        filter_str = kwargs["where"].format(*[str(item) for item in kwargs["whereArg"]])
        sql_str = f"{sql_str}\nWHERE {filter_str}"
    elif "where" in kwargs:
        # just where in kwargs
        if not isinstance(kwargs["where"], str):
            raise ValueError("where should be a string.")
        sql_str = f"{sql_str}\nWHERE {kwargs['where']}"
    elif "whereArg" in kwargs:
        # just whereArg in kwargs
        raise ValueError("must have a string argument named where if obtain whereArg.")

    return sql_str


if __name__ == '__main__':
    # just a table name
    sql_str = sql_generate("student")
    print(sql_str, "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sql_str = sql_generate("student", columns=["id", "name", "sex", "grade"])
    print(sql_str, "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sql_str = sql_generate("student", columns=["id", "name", "sex", "grade"], where="sex = 0 and grade = 1")
    print(sql_str, "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sql_str = sql_generate("student", columns=["id", "name", "sex", "grade"], where="{} = 0 and {} = 1",
                           whereArg=["sex", "grade"])
    print(sql_str, "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

########################################################################################################################
# Result run at 7/5/2021 11:08 PM                                                                                      #
#                                                                                                                      #
# SELECT *                                                                                                             #
# FROM student                                                                                                         #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                                                                    #
# SELECT id, name, sex, grade                                                                                          #
# FROM student                                                                                                         #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                                                                    #
# SELECT id, name, sex, grade                                                                                          #
# FROM student                                                                                                         #
# WHERE sex = 0 and grade = 1                                                                                          #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                                                                    #
# SELECT id, name, sex, grade                                                                                          #
# FROM student                                                                                                         #
# WHERE sex = 0 and grade = 1                                                                                          #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                                                                    #
########################################################################################################################
