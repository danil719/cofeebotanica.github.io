import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent
import re
import random
from main import *


categoryCurl = input('Введите ссылку на первую страницу выбранной категории (например https://www.m.podrygka.ru/catalog/ukhod/): ')
countPageCurl = '?PAGEN_1='
countSearch = input('Введите количество страниц которое нужно добавить на яндекс маркет: ')


for page in range(1, int(countSearch) + 1):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": "utm_source=0; BITRIX_SM_utm_source=0; utm_medium=0; BITRIX_SM_utm_medium=0; utm_campaign=0; BITRIX_SM_utm_campaign=0; utm_content=0; utm_term=0; click_id=0; BITRIX_SM_SALE_UID=1450882741; rrpvid=503046113681022; rcuid=65e233272878efb2881c19a2; _gcl_au=1.1.1065764992.1719346734; _ga=GA1.1.1167264929.1719346736; _ym_uid=1719346737998852725; _ym_d=1719346737; tmr_lvid=18009f739fcfd2e87e514ea0d87dd988; tmr_lvidTS=1719346737431; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=c85c9119-b403-4d11-92de-366af03cbe6d; uxs_uid=2b3a1bd0-3330-11ef-89a1-e765ba9be233; analytic_id=1719346745033495; flocktory-uuid=51b9caea-2c14-4e0b-8041-52c1ba76b6e9-5; _ymab_param=IxRqi43jKqQUVVz7yAIRj4TF5mZZpDA0Xsl3EQqFRiYwU7FXZSW5qD6sIdYlC6N1Co07CXD7lg7lotrYIBi_ePLFXaI; _userGUID=0:lxx6a4z0:Vbhg2kOLPAx_YjmDrKXSfWSkKb21Po3W; Fuuid=965dccde-2527-4442-aa2f-cfb61dc30f3a,1719346737; adid=171948720116283; _ym_isad=2; _ym_visorc=b; PHPSESSID=lvn0b1h6hdr431mpv24v73dg6b; dSesn=a86bae93-1201-ef1d-c5ad-1ee41ae3e25b; _dvs=0:lygbuii7:c8RY0EFILkYn9gpqWE5fbrYQkYbz7gZ1; BITRIX_SM__ym_uid=1719346737998852725; sess_hash=0; domain_sid=G4p0819y1sASwUQc8NXmt%3A1720645407443; Dsign=y; Duuid=279ece0e-eb94-4928-98ee-5ba07d85f19d; searchStartTime=1720645443047; digi_uc=|v:171948:119509:1356803!172064:54751|s:171948:1286606!172064:54751; tmr_detect=0%7C1720645767179; referrer=; deduplication_cookie=simbad; _ga_PNTGGG08RK=GS1.1.1720644509.4.1.1720645772.42.0.0; _ga_PWENEEGPGE=GS1.1.1720644514.4.1.1720645772.0.0.0; BITRIX_SM_utm_source=simbad; BITRIX_SM_utm_medium=cpo; BITRIX_SM_utm_campaign=rore_product_a-b-c_d_ru_2024-06-01_sm; BITRIX_SM_utm_content=cid%3D%7Bcampaign_id%7D--cname%3D%7Bcampaign_name%7D--camtype%3D%7Bcampaign_type%7D--geo%3D%7Bregion_name%7D_%7Bregion_id%7D--srctype%3D%7Bsource_type%7D_%7Bsource%7D--adtarget%3D%7Badtarget_id%7D_%7Badtarget_name%7D--retargeting%3D%7Bretargeting_id%7D--gid%3D%7Bgbid%7D--device%3D%7Bdevice_type%7D--adp%3D%7Baddphrases%7D--adpt%3D%7Baddphrasestext%7D--cgcontextid%3D%7Bcoef_goal_context_id%7D--intid%3D%7Binterest_id%7D; BITRIX_SM_utm_term=aid%3D%7Bad_id%7D--key%3D%7Bkeyword%7D--phrid%3D%7Bphrase_id%7D--pos%3D%7Bposition_type%7D_%7Bposition%7D--matchkey%3D%7Bmatched_keyword%7D--match%3D%7Bmatch_type%7D--targ%3D%7Badtarget_name%7D; _ga_QEX3SJGQ13=GS1.1.1720644509.4.1.1720645772.0.0.0; advcake_track_id=04075896-4925-179c-d415-36cda988f9f1; advcake_session_id=05c58b55-e310-5a1c-d627-e724110712d8; advcake_track_url=!CRACExJRSk4TARRPGwoFFg8ECgpLExFZXBQfCD4XGRYTCABcFx8OAwoBRxECDj4GAAUNAw5cCBUOQgMXDDQGAAkGAggMC1wWGREENBUTCxIWAh86AEkUTgI0AT4WAzxTW1dVSUZVTFtUPhcbRRQfCD4QExEMVgQIAEtGVikEBTsfB0RcIUxJHQYYVkBWJh0GGBwKEwBTVCVGSBEMBAoFVkBWJgYLEwoWBDsfB0RcIUxJBgwSVkBWJgYMEgIRCAsYPBUSFQRBQSc%2BTlIjFBkQCB8MDgpTVCVGSAwFAgAJAAAYWVNUIwYEFQceBgU0DgQdAQwTD0BWIFtODAoRAgxLRlYpCAAQFQs%2BHxwRAVNUJUZIFQUEBFxOUiMFEhcAGQIEECkNAAYARFMyRRQfCD4HGQ0VDgsVWRUKBVZAViYVAgwbBAgDGDwID0BWIFtOAgUEDAFLRlYpBgAJBgIIDAs%2BChcOBE5SJUlbAAAGERgUE15EXCcCBRsTAAICDzsCGhEOQFYgW04GDgpcQUEhEw4CCAsYPA8KCARBQSc%2BTlIjFhMECAQLPg0SRlYvSEwXBAAVEhUEWVNUIxgKFBYVBj4fHBEBU1QlNEBWJgUMFBkGBEFBJ0xGBAUQFxEGDhFcQUEhAA8RABYRBhU0DAVBQSc%2BTlIjBRIXABkCBBApDQAGAERTMk5MGQAVBQQEBB8MDwNLRlYpFwQQFxEGDhEIChE8CA9AViBbTgYCAVxBQSEGCQwFQUEnTEYBBBIfAARWQFYmEgYXAgYEOwIaEQ5AViBbTgAPFVxBQSEADwERDAQCEg4WRFMyTkwKAREQS0ZWKQQFAAYLEwoWBBcCBhkfQFYgW04CDAYOCgIGGR8MBVlTVCMICgQCKQQOCgk%2BBxkNFQ4dFTsfB0RcIUxJHw0VAgFcQUEhCAURBBYTEBU0DAVBQSc%3D; advcake_utm_partner=rore_product_a-b-c_d_ru_2024-06-01_sm; advcake_utm_webmaster=cid; advcake_click_id=",
        "User-Agent": str(UserAgent().random)
    }
    
    response = requests.get(f'{categoryCurl}{countPageCurl}{page}', headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    items = soup.find_all('div', class_='products-list-item__header')
    for takeInf in items:
        curlRest = 'https://www.m.podrygka.ru' + takeInf.find('a').get('href')
        print(curlRest)
        response = requests.get(curlRest, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        nameProduct = soup.find('h1').text
        print(nameProduct)
        
        article = soup.find('div', class_='rr-mobile-show').get('data-product-id').strip()
        print(article)
        
        photoProduct = 'https://www.m.podrygka.ru' + soup.find('div', class_='product-detail__gallery').find('img').get('src')
        print(photoProduct)
        descriptionProduct = soup.find('div', class_='__text').text
        print(descriptionProduct)
        priceProduct = soup.find('span', class_='product-detail-price-wrapper__price__current-price').text.replace('₽', '').strip()
        if int(priceProduct)*3<350:
            priceProduct='350'
        else:
            priceProduct = str(int(priceProduct)*3)
        vendorProduct = f'podrygka-{article}'
        barcodesProduct = random.randint(1000000000, 9999999999)
        vendorCodesProduct = f'podrygka-{article}'
        marketSku = random.randint(1000000000, 9999999999)
        CreateProductDATA(nameProduct, photoProduct, vendorProduct, barcodesProduct, descriptionProduct, vendorCodesProduct, marketSku, priceProduct)
        break