#!/usr/bin/python
# Author: Danny Yu
from os.path import join
content_title = "COMPANY: "
content_impact = "\nImpact Assessment\n=================\n"
content_install = "\n\nInstall Instructions\n====================\n" + \
                  "Select the target environment.\n" + \
                  "Backup the files.\n" + \
                  "Deploy the files from the release folder to the target environment.\n"
content_rollback = "\n\nRollback Instructions\n=====================\n" + \
                  "Select the target environment.\n" + \
                  "Restore backup of files from the backups folder to the target environment.\n"
content_testing = "\n\nTesting\n=======\n"


def content_func():
    return content_title+content_impact+content_install+content_rollback+content_testing


def input_func():
    global content_title
    global content_impact
    global content_install
    global content_rollback
    global content_testing
    input_whether_enum = {
        "Yes": True,
        "Y": True,
        "yes": True,
        "y": True,
        "No": False,
        "N": False,
        "no": False,
        "n": False
    }

    def whether_question_handler(question, pos_str, neg_str):
        while True:
            user_input = input(question)
            value = input_whether_enum.get(user_input, None)
            if value is not None:
                if value:
                    return pos_str
                else:
                    return neg_str

    # input for company name
    content_title += input("Enter the company ID:")+"\n\n"
    # input for test environment
    content_testing += "Testing occurred in " + \
                       input("Enter the test environment name:") + \
                       "\nTest plan available in the release folder\n"
    # input for environments down time question
    que_impact_env = "Down time of environments?(Yes/No)"
    str_impact_env_pos = "Down time of environments expected.\n"
    str_impact_env_neg = "No down time of environments.\n"
    content_impact += whether_question_handler(que_impact_env, str_impact_env_pos, str_impact_env_neg)
    # input for dll question
    que_impact_dll = "DLL update?(Yes/No)"
    str_impact_dll_pos = "DLL File.\n"
    str_impact_dll_neg = "There is NO DLL involved.\n"
    res_impact_dll = whether_question_handler(que_impact_dll, str_impact_dll_pos, str_impact_dll_neg)
    content_impact += res_impact_dll
    # input for SQL question
    que_impact_sql = "SQL updated?(Yes/No)"
    str_impact_sql_pos = "SQL updated.\n"
    str_impact_sql_neg = "There is NO SQL involved.\n"
    res_impact_sql = whether_question_handler(que_impact_sql, str_impact_sql_pos, str_impact_sql_neg)
    content_impact += res_impact_sql
    if res_impact_sql == str_impact_sql_pos:
        content_install += "Run the SQL scripts in the release folder.\n"
        content_rollback += "Run the Rollback SQL scripts in the release folder.\n"
    # input for schema question
    que_impact_schema = "Schema changed?(Yes/No)"
    str_impact_schema_pos = "Schema File.\n"
    str_impact_schema_neg = "No schema changed.\n"
    content_impact += whether_question_handler(que_impact_schema, str_impact_schema_pos, str_impact_schema_neg)
    # input for flow question
    que_impact_flow = "Flow changed?(Yes/No)"
    str_impact_flow_pos = "Flow change.\n"
    str_impact_flow_neg = "No flow change.\n"
    res_impact_flow = whether_question_handler(que_impact_flow, str_impact_flow_pos, str_impact_flow_neg)
    content_impact += res_impact_flow
    if res_impact_flow == str_impact_flow_pos:
        content_install += "Download flow in the target environment as backup.\n" +\
                           "Migrate the flow in the release folder to the target environment.\n" + \
                           "Refresh the flow.\n"
        content_rollback += "Migrate the flow in the backup folder to the target environment.\n" + \
                            "Refresh the flow.\n"
    return


try:
    input_func()
    fh = open(join("/Users/yud/Desktop", "Release Note.txt"), "w")
    fh.write(content_func())
except IOError:
    print("Error: Fail to load the file.")
else:
    print("Release Note created successfully.")
    fh.close()



