from bs4 import BeautifulSoup
import copy
import os






# Read the HTML content from index.html
with open("Insta to Bootstrap\Template.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

def first_filters(category):
    category_container = soup.find('ul',{'id':'portfolio-flters'})
    filter_option = soup.new_tag('li')
    filter_option['data-filter'] = '.filter-'+str(category)
    filter_option.string = str(category)
    category_container.append(filter_option)
    
    category_container = soup.prettify()

    with open("index.html", "w") as f:
            f.write(category_container)
            print('done with filters')

def post_field(folder,category = None):
    

    
    container = soup.find('div',{'class': 'portfolio-container'})
    filter_div = soup.new_tag('div')
    if category:
        filter_div['class'] = 'col-lg-3 col-md-6 portfolio-item filter-' + str(category)
    else: 
        filter_div['class'] = 'col-lg-3 col-md-6 portfolio-item '
    portfolio_wrap = soup.new_tag('div')
    portfolio_wrap['class'] = 'portfolio-wrap'
    img_container = soup.new_tag('img')
    img_container['class'] = 'img-fluid'
    try:
        print(os.path.join(os.path.basename(folder),os.listdir(folder)[0]), 'loook')
    except IndexError as e:
        print(folder + 'has is an empty folder, please delete it or add proper files')
        if input('want to delete? submit y') == 'y':
            os.rmdir(folder)
            return
        else:
            return

        
    img_container['src'] = os.path.join(folder,os.listdir(folder)[0])
    portfolio_wrap.append(img_container)
    info_div =  soup.new_tag('div')
    info_div['class'] = 'portfolio-info'

    portfolio_wrap.append(info_div)

    portfolio_links_div =  soup.new_tag('div')
    portfolio_links_div['class']= 'portfolio-links'
    slider_link1 = soup.new_tag('a')
    print(str(os.path.join(folder,os.listdir(folder)[0])))

    slider_link1['href'] =  os.path.join(folder,os.listdir(folder)[0])

    slider_link1['title'] = 'Example title'
    slider_link1['class'] = 'portfolio-lightbox'
    slider_link1['data-gallery'] = os.path.basename(folder)
    portfolio_linksI =  soup.new_tag('i')
    portfolio_linksI['class'] = 'bx bx-plus'
    slider_link1.append(portfolio_linksI)
    slider_link2 = soup.new_tag('a')

    slider_link2['href'] =  'https://www.' + str(os.path.basename(folder)).replace('-','/')
    slider_link2['class']= "More Details"
    slider_link2['target'] ="_blank"
    portfolio_links2I =  soup.new_tag('i')
    portfolio_links2I['class'] = "fa fa-instagram"
    slider_link2.append(portfolio_links2I)
    portfolio_links_div.append(slider_link1)
    portfolio_links_div.append(slider_link2)
    portfolio_wrap.append(portfolio_links_div)

    for photo in os.listdir(folder)[1::]:
            photo_link = os.path.join(folder,photo)
            photo_linkA = soup.new_tag('a')            
            photo_linkA['class'] = 'portfolio-lightbox'
            photo_linkA['data-gallery'] = os.path.basename(folder)
            photo_linkA['href'] = photo_link

            portfolio_wrap.append(photo_linkA)
    
    filter_div.append(portfolio_wrap)
    
    container.append(filter_div)
    
    container = soup.prettify()

    with open("index.html", "w") as f:
            f.write(container)
            print('dome')



  
  
      
pathway = "Insta to Bootstrap\Categories_folder"

def category_level_down(head_folder):
    for category in os.listdir(head_folder):
        print(category)
        first_filters(str(os.path.basename(category)))
        category_path = os.path.join(head_folder,category)
        for folder in os.listdir(category_path):
            print(folder)
            post_field(os.path.join(category_path,folder),str(os.path.basename(category_path)))
                

category_level_down(pathway)
