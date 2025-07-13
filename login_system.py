def login_system():
    list = [{"name":"omar","pass":"123"},{"name":"ali","pass":"444"}]
    
    name = input("enter ur name : ")
    for i in list:
        if name == i["name"]:
            pas = input('enter ur pass: ')
            if pas == i["pass"]:
                return {"status": "success", "user": name}
            else:
                return {"status": "wrong_password"}
    return {"status": "user_not_found"}