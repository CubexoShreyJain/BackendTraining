import mysql.connector


cur = None

def show(query, *args):
    
    if args:
        cur.execute(query, args)
    else:
        cur.execute(query)
    res = cur.fetchall()
    for i in res:
        print(i)
    print()

def run(query):
    
    cur.execute(query)
    

if __name__ == '__main__':

    conn = mysql.connector.connect(
        host= "localhost",
        user= 'shrey',
        password= 'Shrey@5051',
        database='cubexo'
        )

    cur = conn.cursor()
    
    show("Describe cubexo;")
    # run("create database cubexo;")
    print("Tables: ")
    show("show tables;")
    show("select * from cubexo;")
    
    #Injection testing
    u_id = input("Enter your user id: ")
    print("First")
    show(f"SELECT * FROM cubexo WHERE e_id= {u_id}") # '' or 1=1 
    
    print("Second")
    show(f"SELECT * FROM cubexo WHERE e_id= %s", u_id) # Injection didn't worked (Prevention technique)
    # show(f"SELECT ")
    
    dep = input("Enter Department code: ")
    print("3. By departement: ")
    show(f"SELECT * FROM cubexo where dep_code = '{dep}'") # ' OR ''='
    
    print("And injection")
    show(f"SELECT * FROM cubexo WHERE e_id = {u_id} AND dep_code = '{dep}'") # u_id = "" or ''='' dep = ' or ''='
    
    # Bached injection (Multiple query in single line. Connected using ;)
    # SELECT * from cubexo where uid = 3; drop table cubexo // is a valid query 
    
    bached = input('Enter bached user id: ')
    show(f'SELECT * FROM cubexo where e_id = {bached};') # ''; drop test;
    
    print("Tables: ")
    show("show tables;")
    
    """
    Prevention: 
    
    We use parameteres to pass variables. As they are check by the engine before passing. 
    It only pass the intended values and datatypes and reject any executable query.
    We can pass any number of parameter with just using '@' sign. 

    """
    # % is used in connector and an iterable is passed to executor
    print("First")
    show("Select * from cubexo where e_id = %s;", u_id)
    print("Second")
    show("select * from cubexo where e_id = %s AND dep_code = %s;", u_id, dep)
    
    cur.close()
    conn.close()