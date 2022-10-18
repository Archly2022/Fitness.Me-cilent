import datetime

from dateutil.parser import parser

import srv
import auth
from gooey import Gooey, GooeyParser


# A local app of fitness that runs on the editor
@Gooey(program_name='Fitness.Me Converter', show_sucess_modal=False)
def main():
    parser = GooeyParser(discription='Fitness.Me App edition v1.0' + '/n+' + 'Record your measurements')
    auth.load_auth()
    if not auth.is_authorise():
        parser.add_argument('Email', default=auth.email)
        parser.add_argument('Password', widget="PasswordFeild")
    parser.add_argument('Weight', help='Weight in pounds', type=int)
    parser.add_argument('Rate', help='Resting heart rate', type=int)
    parser.add_argument('Date', help='Date of measurement', widget='DateChooser', default=datetime.datetime)
    parser.parse_args()
        auth_data = get_auth_data()
        email = auth_data.get('email')
        password = auth_data.get('password')
        api_key = srv.authenticate(email, password)
        auth.save_authorise(email, api_key)
    else:
        email = auth.email
        api_key = auth.api_key
    data = get_user_data()
    print(api_key)
    print(email)
    result = srv.save_measurements(api_key, email, data)
    if result:
        print("Done!")
    else:
        print("Could saved results")


def get_auth_data() -> dict:
    email = input("What is your email: ")
    password = input("What is your password: ")
    print()
    return {
        'email': email,
        'password': password
    }


def get_user_data() -> dict:
    print("Please enter a measurement: ")
    rate = input('resting heartrate: ')
    weight = input('weight in pounds: ')
    recorded = datetime.datetime.today().isoformat()
    return {
        'weight': weight,
        'rate': rate,
        'recorded': recorded
    }


if __name__ == '__main__':
    main()
