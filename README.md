# Flask Authentication

## Learning Goals

- Use the session object to authenticate a user

- Securely store the password in a hash

- Use the session object to determine when a user is logged in

- Authorize only certain resources depending on whether a user is logged in

## Getting Started

Fork / clone the repo and run
```bash
pipenv install
```

To start the server:
```bash
pipenv shell
cd server
flask db upgrade
python app.py
```

To start the client, create a separate terminal and run:
```bash
npm install --prefix client
npm run dev --prefix client
```


## Additional Resources

[MDN Using HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

[Flask Session](https://flask-session.readthedocs.io/en/latest/)

[Vite + React Proxying API Requests](https://vitejs.dev/config/server-options#server-proxy)

[Create React App Proxying API Requests](https://create-react-app.dev/docs/proxying-api-requests-in-development/)

[Python Generating Secrets](https://docs.python.org/3/library/secrets.html)