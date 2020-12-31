from apps.hotdeal.models import HotDeal
from django.db import IntegrityError

class HotdealscraperPipeline:
    def process_item(self, item, spider):
        if not item:
            return 
       
        photo = None
        
        if item['images']:
            photo = item['images'][0]['path']
        
        try:
            hotdeal = HotDeal.objects.create(
                title = clean_title(item['title']),
                site = item['site'].strip(),
                url = item['url'],
                category = item['category'], 
                site_post_id = item['site_post_id'], 
                photo = photo
            )
        except IntegrityError:
            print(f'already created {item["title"]}')

        return item



def clean_title(param):
    return param.strip()

def clean_critics_consensus(param):
    return ' '.join(param)

def clean_average_grade(param):
    param = param
    return param

def clean_poster(param):
    if param:
        param = param[0]['path']
    return param

def clean_amount_reviews(param):
    return param.strip()

def clean_approval_percentage(param):
    return param.strip().replace('%', '')


