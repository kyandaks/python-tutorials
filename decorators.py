#used a lot in django @login_required @permission_required

def permission_dec(func):

    def func_wrapper():
        #code before function
        print('please login to see secrets and list of presidents')
        func()
        #code after function
        print('you are logged in and permitted')

    return func_wrapper

@permission_dec
def secrets():
    print('here are Ugandan secrets since 1900')

secrets()

@permission_dec
def view_ugandan_presidents():
    print("Uganda's presidents: Museveni Yoweri, Ignatius Musaazi, Tito Okello, Obote Milton ...")

view_ugandan_presidents()