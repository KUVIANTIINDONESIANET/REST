from requests import Session
from bs4 import BeautifulSoup as bs

r = Session()

class tp:
    def __init__(self):
        self.BaseUrl = 'https://textpro.me{}'
        self.theme = {
            'pornhub': '/pornhub-style-logo-online-generator-free-977.html',
            'wolf_galaxy': '/create-wolf-logo-galaxy-online-936.html',
            'sky_online': '/create-a-cloud-text-effect-in-the-sky-online-997.html',        
            'black_pink': '/create-blackpink-logo-style-online-1001.html',
            'marvel_studio': '/create-logo-style-marvel-studios-online-971.html',
            'glitch': '/create-glitch-text-effect-style-tik-tok-983.html'
        }

    def pornhub(self, text, text2):
        '''
        text = white text
        text2 = black text
        '''
        try:
            url = self.BaseUrl.format(self.theme['pornhub'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text,u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR CUK'
            }

    def wolf_galaxy(self, text, text2):
        '''
        text = top text
        text2 = center text
        '''
        try:
            url = self.BaseUrl.format(self.theme['wolf_galaxy'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text, u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR CUK'
            }

    def glitch(self, text, text2):
        '''
        text = top text
        text2 = center text
        '''
        try:
            url = self.BaseUrl.format(self.theme['glitch'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text, u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR CUK'
            }


    def sky_online(self, text):
        '''
        text = text
        '''
        try:
            url = self.BaseUrl.format(self.theme['sky_online'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {'text[]': text, 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR CUK'
            }

    def black_pink(self, text):
        '''
        text = text
        '''
        try:
            url = self.BaseUrl.format(self.theme['black_pink'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {'text[]': text, 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR CUK'
            }

    def marvel(self, text, text2):
        '''
        text = Marvel
        text2 = Studio
        '''
        try:
            url = self.BaseUrl.format(self.theme['marvel_studio'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text, u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR CUK'
            }
