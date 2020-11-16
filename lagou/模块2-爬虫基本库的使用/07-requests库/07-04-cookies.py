import requests

cookies = '_ga=GA1.2.889107264.1604828975; tz=Asia%2FShanghai; _octo=GH1.1.1460131334.1604828975; _device_id=fc8ca229ee955a14a2feb095d78671d3; has_recent_activity=1; user_session=wttOiXXO6QAG6tpcjzdMabBScxYJLiOi4Rvwk3k6j07ejUcs; __Host-user_session_same_site=wttOiXXO6QAG6tpcjzdMabBScxYJLiOi4Rvwk3k6j07ejUcs; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=liumengge; _gh_sess=6maWxErgclq3A2L7zC82Mt5u%2BjqGSuC8Y7do%2B1ZWJsOJBFPgfzap0lwv%2Fd%2BzJLhJ%2F9N%2B%2FvR2%2FZa6G%2BMH5FH%2BEDRdl3SjZ5sBSLfBqfEoBw5921tY%2BJQfWAp0kFcmjda6KrtvcsyBMalJMvX0wicqY4s6RpNGFMZk%2BuOGotu1znyNFgZkC9OhNMZjCkrjHv7sTyKz8actNEQd1ihoQ%2B57LSDcPALRgtb96K9rWB7A%2Fc44BW82I4R04oM19Txkokft3lkcwYeBsMYwUKqpnH9k0vhHcTFDdk1%2F95%2BtqNL7QjM1mxUymjijsc37q9LOJ0ZDkzzteALA2zm5K2h%2BAZRbQpO6qmUkKuin7MCM0jlCz7y4jJJ6u2J9Y2EJjEsYV5RqXDK32hYn0K67NGy%2FTOSrNvx9pRj%2FkzjU%2B09RLC4xRBf9Yt1BQx%2FV0gfgZ%2FsUJgSt9VdIsv%2BiS4eR9yhYjwzLShxtxSGs%2BKn3GQJLAD2JFZJqz9wSTw%2BGzGELA5AbgwNlaOT%2BgbNygg5J%2FqSljJtE01h8MNyYTxbocuskhBhTaiTICwzwsfyDizlBQm38uZkgChjLUUB4Nk3E5EpeykpSw%2FG5elCSXoONhn1DeGWCTrai%2FgQhQnSSXn9XezuP9BeB2bV7bUN45odFscxT8YATlkYsiLK6vYUIrz361lHkh5y0WIPT8N%2BHhfseGbMgViZN%2FRum0yrAxVDjNpDhABm005gsbsh%2FiCM4PxFBjuKU8hvZR5WqeUTJrj5tlX5SYlN7v2BQJNTwIUPAPZ0qhNNVWwgKwpyWmhrDlSLynWUXlARhGedqqGPE292ZtKWW%2FQ5%2FMY1GS824kljXLtRT%2Ft%2BjLq8X%2FcdCYvhM6Qyb7Z7iGX4AYw%2BSKkudqqh98AQCCWaPllI%2BK%2BonDTSavxoe8kJ7wP5WZPX2CDwLKfCULw%3D%3D--2qznvRmhWrdi0YdS--gXbjgsxZ6hLl9NIDGQvVrQ%3D%3D'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)

r = requests.get('https://github.com/', cookies=jar, headers=headers)
print(r.text)
