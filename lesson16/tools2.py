class Taiwan_AQI():    
    API_KEY = "55910016-2e58-4d25-b686-4383e0a0dee6"
    @classmethod
    def download_aqi(cls):
        import requests
        response=requests.get(f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')
        
        print(response.text)