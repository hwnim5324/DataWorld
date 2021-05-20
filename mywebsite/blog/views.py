from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Title, Tag
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

   
def index(req):
    #파일 열어서 값 저장

    test = [0,1,2,3]
    text = "hi"
    template = loader.get_template('index.html')
    context = {
        'test' : test[2],
        'text' : text
    }

    return render(req, 'index.html', context)



@csrf_exempt
def selectTitle(req):
    tagResult = {"Architecture":[['BigBackgroundImages','Clean','ContentArchitecture','Animation','Minimal'],['CSS3','Wordpress','Bootstrap','HTML5','PHP']],
    "Art & Illustration":[['Animation','Colorful','Illustration','GraphicDesign','Clean'],['CSS3','HTML5','WebGL','Wordpress','SVG']],
    "Business & Corporate":[['Animation','Clean','BigBackgroundImage','Colorful','ResponsiveDesign'],['CSS3','Wordpress','HTML5','SVG','Bootstrap']],
    "Culture & Education":[['Animation','Colorful','Clean','Fullscreen','ResponsiveDesign'],['CSS3','HTML5','Wordpress','SVG','CSSFramework']],
    "Design Agencies":[['Animation','Clean','Colorful','Fullscreen','ResponsiveDesign'],['CSS3','Wordpress','SVG','GSAPAnimation','CSSFramework']],
    "E-Commerce":[[ 'Clean','BigBackgroundImages','ResponsiveDesign','Animation','Colorful'],['Shopify','WooCommerce','Wordpress','CSS3','HTML5']],
    "Events":[['Colorful','Animation','BigBackgroundImages','Clean','Fullscreen'],['CSS3','Wordpress','SVG','HTML5','PHP']],
    "Experimental":[['3D','Animation','InteractionDesign','Colorful','FiltersAndEffects'],['Three.js','WebGL','GLSL','CSS3','GSAPAnimation']],
    "Fashion":[['Clean','BigBackgroundImages','Animation','Minimal','Colorful'],['Shopify','WooCommerce','CSS3','HTML5','Wordpress']],
    "Film & TV":[['Video','Animation','Fullscreen','BigBackgroundImages','FiltersAndEffects'],['CSS3','HTML5','WebGL','Wordpress','Three.js']],
    "Food & Drink":[['Animation','BigBackgroundImages','Colorful','Clean','Fullscreen'],['CSS3','Wordpress','HTML5','SVG','Shopify']],
    "Games & Entertainment":[['Animation','Colorful','3D','Fullscreen','Illustration'],['WebGL','Three.js','CSS3','HTML5','GSAPAnimation']],
    "Hotel / Restaurant":[['BigBackgroundImages', 'Animation', 'Clean', 'ResponsiveDesign', 'AppStyle'],['CSS3', 'Wordpress', 'CSSFramework', 'HTML5', 'SVG']],
    "Institutions":[['BigBackgroundImages', 'Contentarchitecture', 'Colorful', 'Clean', 'Animation'],['WooCommerce', 'CSS3', 'Drupal', 'Wordpress', 'PHP']],
    "Magazine / Newspaper / Blog":[['Clean', 'Colorful', 'BigBackgroundImages', 'Animation', 'Minimal'],['Wordpress', 'CSS3', 'HTML5', 'PHP', 'Magento']],
    "Mobile & Apps":[['Animation', 'Colorful', 'Clean', 'ResponsiveDesign', '3D'],['CSS3', 'HTML5', 'WebGL', 'CSSFramework', 'SVG']],
    "Music & Sound":[['Animation', 'Colorful', 'AppStyle', 'FullScreen',  'Video'],['WebGL', 'CSS3', 'HTML5', 'Three.js', 'GSAPAnimation']],
    "Other":[['Animation', 'BigBackgroundImages', 'Clean', 'Colorful', 'Fullscreen'],['CSS3', 'Wordpress', 'HTML5', 'SVG', 'jQuery']],
    "Photography":[['BigBackgroundImages', 'Clean', 'Animation', 'GraphicDesign', 'Minimal'],['CSS3', 'HTML5', 'Wordpress', 'CSSFramework', 'Shopify']],
    "Promotional":[['Animation', 'BigBackgroundImages', 'Clean', 'Colorful', 'Fullscreen'],['CSS3', 'HTML5', 'GSAPAnimation', 'WebGL', 'SVG']],
    "Real Estate":[['BigBackgroundImages', 'Animation', 'Clean', 'Contentarchitecture', 'AboutPage'],['Shopify', 'Bootstrap', 'Wordpress', 'CSS3', 'CSSFramework']],
    "Sports":[['BigBackgroundImages', 'Animation', 'Fullscreen', 'Clean', 'ResponsiveDesign'],['CSS3', 'Bootstrap', 'CSSFramework', 'HTML5', 'Anime.js']],
    "Startups":[['Animation', 'Clean', 'Colorful', 'AboutPage', '3D'],['CSS3', 'HTML5', 'Shopify', 'FastClick', 'Wordpress']],
    "Technology":[['Animation', 'Clean', 'Colorful', '3D', 'BigBackgroundImages'],['CSS3', 'HTML5', 'WebGL', 'SVG', 'Wordpress']],
    "Web & Interactive":[['Animation', 'Clean',  'Colorful', '3D', 'InteractionDesign'],['CSS3', 'HTML5', 'WebGL', 'Three.js', 'GSAPAnimation']] 
    }

    if 'title_key' in req.POST:
        current_title = req.POST['title_key']

    before_title = get_object_or_404(Title,pk=3) #이전 저장되어있는 주제 
    if current_title in list(tagResult.keys()):
        is_exist = True
        tags=tagResult[current_title]
        title = Title.objects.get(pk=3)
        title.title = current_title
        title.save()
        before_title = get_object_or_404(Title,pk=3)
    else:
        is_exist = False
        tags=[['Tag1','Tag2','Tag3','Tag4','Tag5'],['Tag1','Tag2','Tag3','Tag4','Tag5']]
        before_title = get_object_or_404(Title,pk=3)


    context = {
        'is_exist':is_exist,
        'title':current_title,
        'designTag1':tags[0][0],
        'designTag2':tags[0][1],
        'designTag3':tags[0][2],
        'designTag4':tags[0][3],
        'designTag5':tags[0][4],
        'techTag1':tags[1][0],
        'techTag2':tags[1][1],
        'techTag3':tags[1][2],
        'techTag4':tags[1][3],
        'techTag5':tags[1][4],
    }
    return JsonResponse(context) 


@csrf_exempt
def selectTag(req):
    url_result = {
        "BigBackgroundImages":[['https://whocares.bigbump.fr/','https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'],['https://whocares.bigbump.fr/','https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'],['https://whocares.bigbump.fr/','https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'],['http://www.pbs.up.pt','https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg'],['https://whocares.bigbump.fr/','https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        "Clean":[['https://antara.studio/', 'https://assets.awwwards.com/awards/sites_of_the_day/2021/02/antara-1.jpg'], ['https://getuniq.me/en/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa5416cd35a4668902276.jpg'], ['https://mariacerdan.com', 'https://assets.awwwards.com/awards/submissions/2020/11/5fc57758bd897373737031.jpg'], ['https://andreaspsaltis.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8755379be69216727738.png'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg']],
        'ContentArchitecture':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['https://livingedge.com.au/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd9a1c135ff6945266098.png'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg']],
        "Animation":[['https://lilkleine.nl','https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'],['https://getuniq.me/en/','https://assets.awwwards.com/awards/submissions/2020/11/5fa5416cd35a4668902276.jpg'],['http://eyezen-challenge.com','https://assets.awwwards.com/awards/sites_of_the_day/2016/04/awwwards-sotd-Eyezen-Challenge-1.jpg'],['https://visitevirtuelle.avoriaz.com','https://assets.awwwards.com/awards/submissions/2020/12/5fc907a7893f7417689154.jpg'],['https://whocares.bigbump.fr/','https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        'Minimal':[['https://wemakefab.school', 'https://assets.awwwards.com/awards/submissions/2021/01/5fff1daf2b6e2165463343.jpg'], ['https://www.zwislerdecker.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd940f4ab70e326608722.png'], ['https://www.gtheimagineers.com/', 'https://assets.awwwards.com/awards/submissions/2020/09/5f6e38761ccb6699232404.png'], ['https://andreaspsaltis.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8755379be69216727738.png'], ['https://www.zwislerdecker.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd940f4ab70e326608722.png']],
        'CSS3':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://www.zwislerdecker.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd940f4ab70e326608722.png'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'], ['https://visitevirtuelle.avoriaz.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc907a7893f7417689154.jpg'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        'Wordpress':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['https://noel.heschung.com/en/', 'https://assets.awwwards.com/awards/submissions/2020/01/5e15d6e49face084523426.jpg'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png']],
        'Bootstrap':[['https://www.minidil.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8834d056b5d850029997.jpg'], ['https://www.theatredelaville-paris.com', 'https://assets.awwwards.com/awards/submissions/2018/06/5b17e4cd2cad3.jpg'], ['http://www.muffingroup.com', 'https://assets.awwwards.com/awards/submissions/2018/03/5abe07056e6a1.png'], ['https://andreaspsaltis.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8755379be69216727738.png'], ['https://www.minidil.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8834d056b5d850029997.jpg']],
        'HTML5':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['http://eyezen-challenge.com', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/04/awwwards-sotd-Eyezen-Challenge-1.jpg'], ['https://visitevirtuelle.avoriaz.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc907a7893f7417689154.jpg'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        'PHP':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['http://resn.co.nz', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/06/awwwards-sotd-rens-1.jpg'], ['https://www.fcnantes.com', 'https://assets.awwwards.com/awards/submissions/2018/02/5a85a197d440c.jpg'], ['https://www.fcnantes.com', 'https://assets.awwwards.com/awards/submissions/2018/02/5a85a197d440c.jpg']],
        'Colorful':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://getuniq.me/en/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa5416cd35a4668902276.jpg'], ['https://oishiii.sushiya.ua/page6927365.html', 'https://assets.awwwards.com/awards/submissions/2020/04/5e907b35e4e18441111004.png'], ['https://mendeleev.me/', 'https://assets.awwwards.com/awards/submissions/2019/05/5cce28a1ef20f455268300.png'], ['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg']] ,
        'Illustration':[['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'], ['https://getuniq.me/en/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa5416cd35a4668902276.jpg'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        'GraphicDesign':[['http://www.iamfrank.eu', 'https://assets.awwwards.com/awards/submissions/2018/04/5acb592a26f1c.jpg'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['https://oishiii.sushiya.ua/page6927365.html', 'https://assets.awwwards.com/awards/submissions/2020/04/5e907b35e4e18441111004.png'], ['https://kineticnight.com/', 'https://assets.awwwards.com/awards/submissions/2019/05/5cd0cc65e6f48907102147.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg']],
        'HTML5':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['http://eyezen-challenge.com', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/04/awwwards-sotd-Eyezen-Challenge-1.jpg'], ['https://visitevirtuelle.avoriaz.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc907a7893f7417689154.jpg'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        'WebGL':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://www.zwislerdecker.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd940f4ab70e326608722.png'], ['http://eyezen-challenge.com', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/04/awwwards-sotd-Eyezen-Challenge-1.jpg'], ['http://www.because-recollection.com', 'https://assets.awwwards.com/awards/sites_of_the_day/2015/12/recollection-site.jpg'], ['https://kineticnight.com/', 'https://assets.awwwards.com/awards/submissions/2019/05/5cd0cc65e6f48907102147.jpg']],
        'SVG':[['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['https://mark-appleby.com/', 'https://assets.awwwards.com/awards/submissions/2020/08/5f455e587f7f1940047313.png'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg']],
        'ResponsiveDesign':[['http://www.iamfrank.eu', 'https://assets.awwwards.com/awards/submissions/2018/04/5acb592a26f1c.jpg'], ['http://www.purplebunny.co', 'https://assets.awwwards.com/awards/submissions/2019/10/5d9c4fe2e28ad584666482.jpg'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg']],
        'Bootstrap':[['https://www.minidil.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8834d056b5d850029997.jpg'], ['https://www.theatredelaville-paris.com', 'https://assets.awwwards.com/awards/submissions/2018/06/5b17e4cd2cad3.jpg'], ['http://www.muffingroup.com', 'https://assets.awwwards.com/awards/submissions/2018/03/5abe07056e6a1.png'], ['https://andreaspsaltis.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8755379be69216727738.png'], ['https://www.minidil.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8834d056b5d850029997.jpg']],
        'Fullscreen':[['http://www.iamfrank.eu', 'https://assets.awwwards.com/awards/submissions/2018/04/5acb592a26f1c.jpg'], ['https://www.zwislerdecker.com', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd940f4ab70e326608722.png'], ['http://eyezen-challenge.com', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/04/awwwards-sotd-Eyezen-Challenge-1.jpg'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png'], ['https://whocares.bigbump.fr/', 'https://assets.awwwards.com/awards/submissions/2020/11/5fa952256f5ac847399344.png']],
        'CSSFramework':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['https://www.sick7.com', 'https://assets.awwwards.com/awards/submissions/2020/09/5f6ec59b141bd174258874.jpg'], ['https://www.childrenssociety.org.uk/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f7ec541220a0806554410.jpg'], ['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg']],
        'GSAPAnimation':[['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['http://resn.co.nz', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/06/awwwards-sotd-rens-1.jpg'], ['https://verholy.com/en/', 'https://assets.awwwards.com/awards/sites_of_the_day/2021/02/verholy-1.jpg'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png']],
        'Shopify':[['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg']],
        'WooCommerce':[['https://www.lucedisorrento.it/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fcdfaff79a1e991353096.png'], ['https://sassiholford.com', 'https://assets.awwwards.com/awards/submissions/2019/11/5dd2af766a954298873003.jpg'], ['https://www.lucedisorrento.it/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fcdfaff79a1e991353096.png'], ['http://wildatheartfoundation.org', 'https://assets.awwwards.com/awards/submissions/2020/02/5e55177555506146841648.jpg'], ['https://oui.jeandousset.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f906eae53e26617622989.jpg']],
        'PHP':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['http://resn.co.nz', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/06/awwwards-sotd-rens-1.jpg'], ['https://www.fcnantes.com', 'https://assets.awwwards.com/awards/submissions/2018/02/5a85a197d440c.jpg'], ['https://www.fcnantes.com', 'https://assets.awwwards.com/awards/submissions/2018/02/5a85a197d440c.jpg']],
        '3D':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://mark-appleby.com/', 'https://assets.awwwards.com/awards/submissions/2020/08/5f455e587f7f1940047313.png'], ['https://fabricofthenation.com/intro', 'https://assets.awwwards.com/awards/submissions/2020/10/5f81c2262e718750717263.jpg'], ['https://fabricofthenation.com/intro', 'https://assets.awwwards.com/awards/submissions/2020/10/5f81c2262e718750717263.jpg']],
        'InteractionDesign':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['http://zgodanazycie.pl/donation-history', 'https://assets.awwwards.com/awards/submissions/2020/10/5f91468a78844400606306.png'], ['http://zgodanazycie.pl/donation-history', 'https://assets.awwwards.com/awards/submissions/2020/10/5f91468a78844400606306.png'], ['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png']],
        'FiltersAndEffects':[['https://www.cuelr.com', 'https://assets.awwwards.com/awards/submissions/2020/07/5f0ebafe793b9460256165.jpg'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg'], ['https://manosalvas.me/', 'https://assets.awwwards.com/awards/submissions/2019/02/5c6828f611a3f385877318.png'], ['https://www.honeytrapfilm.com/', 'https://assets.awwwards.com/awards/submissions/2020/04/5e85ca3440f7d010793180.jpg'], ['https://gogodigital.com.br', 'https://assets.awwwards.com/awards/submissions/2019/01/5c3cd07fe3b11.jpg']],
        'Three.js':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://mark-appleby.com/', 'https://assets.awwwards.com/awards/submissions/2020/08/5f455e587f7f1940047313.png'], ['https://goodmeat.co/', 'https://assets.awwwards.com/awards/sites_of_the_day/2021/02/goodmeat-1.jpg'], ['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png']],
        'GLSL':[['https://goodmeat.co/', 'https://assets.awwwards.com/awards/sites_of_the_day/2021/02/goodmeat-1.jpg'], ['https://routefifty.caffeina.com/', 'https://assets.awwwards.com/awards/submissions/2019/03/5c91032b34502400899113.jpg'], ['http://resn.co.nz', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/06/awwwards-sotd-rens-1.jpg'], ['https://goodmeat.co/', 'https://assets.awwwards.com/awards/sites_of_the_day/2021/02/goodmeat-1.jpg'], ['https://goodmeat.co/', 'https://assets.awwwards.com/awards/sites_of_the_day/2021/02/goodmeat-1.jpg']],
        'Video':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png'], ['http://eyezen-challenge.com', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/04/awwwards-sotd-Eyezen-Challenge-1.jpg'], ['https://andreaspsaltis.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8755379be69216727738.png'], ['https://analogdigital.tv/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fc8e4bac9b21865223280.png']],
        '3D':[['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://www.sciencepark.at', 'https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'], ['https://mark-appleby.com/', 'https://assets.awwwards.com/awards/submissions/2020/08/5f455e587f7f1940047313.png'], ['https://fabricofthenation.com/intro', 'https://assets.awwwards.com/awards/submissions/2020/10/5f81c2262e718750717263.jpg'], ['https://fabricofthenation.com/intro', 'https://assets.awwwards.com/awards/submissions/2020/10/5f81c2262e718750717263.jpg']],
        'AppStyle':[['https://www.bling.eu/', 'https://assets.awwwards.com/awards/submissions/2020/09/5f72e0be033fd192921261.jpg'], ['https://inkstinct.co', 'https://assets.awwwards.com/awards/submissions/2018/01/5a6ba61577e96.jpg'], ['https://www.bling.eu/', 'https://assets.awwwards.com/awards/submissions/2020/09/5f72e0be033fd192921261.jpg'], ['https://inkstinct.co', 'https://assets.awwwards.com/awards/submissions/2018/01/5a6ba61577e96.jpg'], ['https://www.bling.eu/', 'https://assets.awwwards.com/awards/submissions/2020/09/5f72e0be033fd192921261.jpg']],
        'Drupal':[['https://www.qualityliving.be/', 'https://assets.awwwards.com/awards/submissions/2018/06/5b1f73690fe96.jpg'], ['https://www.childrenssociety.org.uk/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f7ec541220a0806554410.jpg'], ['https://fantasy.bnf.fr/', 'https://assets.awwwards.com/awards/submissions/2020/02/5e539919e688b544191108.jpg'], ['https://www.childrenssociety.org.uk/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f7ec541220a0806554410.jpg'], ['https://www.qualityliving.be/', 'https://assets.awwwards.com/awards/submissions/2018/06/5b1f73690fe96.jpg']],
        'Magento':[['https://www.zenith-watches.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f913f01e7b9b725283080.jpg'], ['https://www.zenith-watches.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f913f01e7b9b725283080.jpg'], ['https://pictowatches.com/', 'https://assets.awwwards.com/awards/submissions/2019/03/5c7e625c00bd3585735073.jpg'], ['https://www.zenith-watches.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f913f01e7b9b725283080.jpg'], ['https://www.zenith-watches.com/', 'https://assets.awwwards.com/awards/submissions/2020/10/5f913f01e7b9b725283080.jpg']],
        'jQuery':[['https://lilkleine.nl', 'https://assets.awwwards.com/awards/submissions/2019/12/5df4ef066436e992593645.jpg'], ['http://lummacups.com', 'https://assets.awwwards.com/awards/submissions/2020/10/5f8768cb4a1e8807939641.jpg'], ['http://resn.co.nz', 'https://assets.awwwards.com/awards/sites_of_the_day/2016/06/awwwards-sotd-rens-1.jpg'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg'], ['http://www.pbs.up.pt', 'https://assets.awwwards.com/awards/submissions/2018/02/5a7ad9538a9d3.jpg']],
        'AboutPage':[['https://bizar.ro/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fd58321dcec8153700112.png'], ['http://www.purplebunny.co', 'https://assets.awwwards.com/awards/submissions/2019/10/5d9c4fe2e28ad584666482.jpg'], ['https://napolitano.io', 'https://assets.awwwards.com/awards/submissions/2020/11/5fad13908759a771019897.jpg'], ['https://kahanipictures.ca/', 'https://assets.awwwards.com/awards/submissions/2020/06/5ef395787fc90493861536.jpg'], ['http://www.purplebunny.co', 'https://assets.awwwards.com/awards/submissions/2019/10/5d9c4fe2e28ad584666482.jpg']],
        'Anime.js':[['https://www.lucedisorrento.it/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fcdfaff79a1e991353096.png'], ['http://ny.paraweb.me', 'https://assets.awwwards.com/awards/submissions/2021/01/5ff8adf9ddc42345850933.png'], ['https://wearezizo.com/', 'https://assets.awwwards.com/awards/sites_of_the_day/2020/02/we-are-zizo-website.jpg'], ['https://www.deniot.com', 'https://assets.awwwards.com/awards/submissions/2020/09/5f6cb6f7e1def568359806.png'], ['https://www.lucedisorrento.it/', 'https://assets.awwwards.com/awards/submissions/2020/12/5fcdfaff79a1e991353096.png']],
        'FastClick':[['https://www.couroazul.com/', 'https://assets.awwwards.com/awards/sites_of_the_day/2018/02/color.jpg'], ['https://4040creative.com.au/', 'https://assets.awwwards.com/awards/submissions/2019/05/5ceb775c21187163313124.jpg'], ['http://springsummer.gucci.com/', 'https://assets.awwwards.com/awards/sites_of_the_day/2018/03/gucci-ss-18-1.jpg'], ['https://4040creative.com.au/', 'https://assets.awwwards.com/awards/submissions/2019/05/5ceb775c21187163313124.jpg'], ['https://4040creative.com.au/', 'https://assets.awwwards.com/awards/submissions/2019/05/5ceb775c21187163313124.jpg']],
    }
    design = ["",""]
    usability = ["",""]
    creativity = ["",""]
    content = ["",""]
    developer = ["",""]

    if 'tag_key' in req.POST:
        select_tag = req.POST['tag_key']
        if not select_tag in ['Tag1','Tag2','Tag3','Tag4','Tag5']:
            urlList = url_result[select_tag]
            site_is_exist=True #필요할까
            design = urlList[0]
            usability = urlList[1]
            creativity = urlList[2]
            content = urlList[3]
            developer = urlList[4]
        else:
            pass

    context={
        'tag':select_tag,
        'designUrl':design[0],
        'designImg':design[1],
        'usabilityUrl':usability[0],
        'usabilityImg':usability[1],
        'creativtyUrl':creativity[0],
        'creativtyImg':creativity[1],
        'contentUrl':content[0],
        'contentImg':content[1],
        'developerUrl':developer[0],
        'developerImg':developer[1]
    }
    return JsonResponse(context)

    '''
    tagResult = {"Architecture":['Business&Corporate','RealEstate','BigBackgroundImages','Other','Photography'], 
    "Art & Illustration":['Culture&Education','Web&Interactive','DesignAgencies','Experimental','Animation'],
    "Business & Corporate":['Technology','Other','DesignAgencies','Promotional','Animation'],
    "Culture & Education":['Art&Illustration','Institutions','Events','Other','Web&Interactive'],
    "Design Agencies":['Web&Interactive','Business&Corporate','Art&Illustration','Animation','Technology'],
    "E-Commerce":['Fashion','Web&Interactive','Business&Corporate','Photography','BigBackgroundImages'],
    "Events":['Culture&Education','Music&Sound','Promotional','Art&Illustration','Business&Corporate'],
    "Experimental":['Web&Interactive','Art&Illustration','Music&Sound','Promotional','Culture&Education'],
    "Fashion":['E-Commerce','Photography','Promotional','Clean','Magazine/Newspaper/Blog'],
    "Film & TV":['Web&Interactive','Promotional','Games&Entertainment','Music&Sound','Video'],
    "Food & Drink":['E-Commerce','Hotel/Restaurant','Promotional','Business&Corporate','Photography'],
    "Games & Entertainment":['Web&Interactive','Promotional','Film&TV','Art&Illustration','Animation'],
    "Hotel / Restaurant":['BigBackgroundImages','Photography','Food&Drink','Film&TV','Animation'],
    "Institutions":['Culture&Education','Other','Business&Corporate','BigBackgroundImages','Events'],
    "Magazine / Newspaper / Blog":['Culture&Education','Web&Interactive','Photography','Clean','Other'],
    "Mobile & Apps":['Web&Interactive','Technology','AppStyle','DesignAgencies','Games&Entertainment'],
    "Music & Sound":['Web&Interactive','Events','Promotional','Art&Illustration','Animation'],
    "Other":['Promotional','Business&Corporate','Web&Interactive','Animation','BigBackgroundImages'],
    "Photography":['BigBackgroundImages','Other','Promotional','Web&Interactive','Business&Corporate'],
    "Promotional":['Web&Interactive','Other','Animation','Business&Corporate','BigBackgroundImages'],
    "Real Estate":['Business&Corporate','Architecture','BigBackgroundImages','Clean','Animation'],
    "Sports":['Promotional','Web&Interactive','BigBackgroundImages','E-Commerce','Animation'],
    "Startups":['Technology','Business&Corporate','Web&Interactive','Animation','Magazine/Newspaper/Blog'],
    "Technology":['Web&Interactive','Business&Corporate','Animation','Startups','Promotional'],
    "Web & Interactive":['Animation','Technology','Promotional','Clean','Colorful'],
    }
    '''

    '''
def result(req):
    tagResult = {"Architecture":['Business&Corporate','RealEstate','BigBackgroundImages','Other','Photography'], 
    "Art & Illustration":['Culture&Education','Web&Interactive','DesignAgencies','Experimental','Animation'],
    "Business & Corporate":['Technology','Other','DesignAgencies','Promotional','Animation'],
    "Culture & Education":['Art&Illustration','Institutions','Events','Other','Web&Interactive'],
    "Design Agencies":['Web&Interactive','Business&Corporate','Art&Illustration','Animation','Technology'],
    "E-Commerce":['Fashion','Web&Interactive','Business&Corporate','Photography','BigBackgroundImages'],
    "Events":['Culture&Education','Music&Sound','Promotional','Art&Illustration','Business&Corporate'],
    "Experimental":['Web&Interactive','Art&Illustration','Music&Sound','Promotional','Culture&Education'],
    "Fashion":['E-Commerce','Photography','Promotional','Clean','Magazine/Newspaper/Blog'],
    "Film & TV":['Web&Interactive','Promotional','Games&Entertainment','Music&Sound','Video'],
    "Food & Drink":['E-Commerce','Hotel/Restaurant','Promotional','Business&Corporate','Photography'],
    "Games & Entertainment":['Web&Interactive','Promotional','Film&TV','Art&Illustration','Animation'],
    "Hotel / Restaurant":['BigBackgroundImages','Photography','Food&Drink','Film&TV','Animation'],
    "Institutions":['Culture&Education','Other','Business&Corporate','BigBackgroundImages','Events'],
    "Magazine / Newspaper / Blog":['Culture&Education','Web&Interactive','Photography','Clean','Other'],
    "Mobile & Apps":['Web&Interactive','Technology','AppStyle','DesignAgencies','Games&Entertainment'],
    "Music & Sound":['Web&Interactive','Events','Promotional','Art&Illustration','Animation'],
    "Other":['Promotional','Business&Corporate','Web&Interactive','Animation','BigBackgroundImages'],
    "Photography":['BigBackgroundImages','Other','Promotional','Web&Interactive','Business&Corporate'],
    "Promotional":['Web&Interactive','Other','Animation','Business&Corporate','BigBackgroundImages'],
    "Real Estate":['Business&Corporate','Architecture','BigBackgroundImages','Clean','Animation'],
    "Sports":['Promotional','Web&Interactive','BigBackgroundImages','E-Commerce','Animation'],
    "Startups":['Technology','Business&Corporate','Web&Interactive','Animation','Magazine/Newspaper/Blog'],
    "Technology":['Web&Interactive','Business&Corporate','Animation','Startups','Promotional'],
    "Web & Interactive":['Animation','Technology','Promotional','Clean','Colorful'],
    }
    #key:tagname, value:url,img
    url_result = {
        "Business&Corporate":[['https://www.sciencepark.at','https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'],['https://getuniq.me/en/','https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'],['https://mariacerdan.com','https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'],['http://www.pbs.up.pt','https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png'],['http://www.pbs.up.pt','https://assets.awwwards.com/awards/submissions/2020/02/5e4fd6ac5f59e508117847.png']],
        "RealEstate":[['https://lighthouseaarhus.dk/',''],['https://lighthouseaarhus.dk/',''],['https://stainedglassvideo.com/',''],['http://www.kosygina21.ru',''],['https://lighthouseaarhus.dk/','']],
        "BigBackgroundImages":[['https://whocares.bigbump.fr/',''],['https://whocares.bigbump.fr/',''],['https://whocares.bigbump.fr/',''],['http://www.pbs.up.pt',''],['https://whocares.bigbump.fr/','']],
        "Other":[['https://www.faitesunvoeu.cc',''],['https://infiniti-online.ru/',''],['https://www.faitesunvoeu.cc',''],['https://www.rivoligroup.com/',''],['https://infiniti-online.ru/','']],
        "Photography":[['',''],['',''],['',''],['',''],['','']],
        "Culture&Education":[['http://www.pbs.up.pt',''],['https://www.theatredelaville-paris.com',''],['http://www.pbs.up.pt',''],['http://www.pbs.up.pt',''],['http://www.pbs.up.pt','']],
        "Web&Interactive":[['https://whocares.bigbump.fr/',''],['https://gogodigital.com.br',''],['http://eyezen-challenge.com',''],['https://whocares.bigbump.fr/',''],['https://whocares.bigbump.fr/','']],
        "DesignAgencies":[['https://antara.studio/',''],['https://gogodigital.com.br',''],['http://www.fold.studio/offline/anagram/',''],['https://antara.studio/',''],['https://gogodigital.com.br','']],
        "Experimental":[['https://krai.co.ua',''],['https://www.sosviolenceconjugale.ca/en',''],['https://mariacerdan.com',''],['https://antyfest.ru/en',''],['https://krai.co.ua','']],
        "Animation":[['https://lilkleine.nl',''],['https://getuniq.me/en/',''],['http://eyezen-challenge.com',''],['https://visitevirtuelle.avoriaz.com',''],['https://whocares.bigbump.fr/','']],
        "Technology":[['https://goodmeat.co/',''],['http://nordichealthhackathon.com/',''],['http://eyezen-challenge.com',''],['https://goodmeat.co/',''],['https://goodmeat.co/','']],
        "Promotional":[['http://www.iamfrank.eu', ''], ['https://getuniq.me/en/', ''], ['http://languagedept.com', ''], ['https://goodmeat.co/', ''], ['https://getuniq.me/en/', '']],
        "Art&Illustration":[['https://whocares.bigbump.fr/', ''], ['https://getuniq.me/en/', ''], ['http://resn.co.nz', ''], ['https://whocares.bigbump.fr/', ''], ['https://whocares.bigbump.fr/', '']],
        "Institutions": [['https://www.minidil.com/', ''], ['https://www.theatredelaville-paris.com', ''], ['http://fremtidensuddannelser.dk/en', ''], ['https://www.theatredelaville-paris.com', ''], ['https://www.minidil.com/', '']],
        "Events":[['http://www.pbs.up.pt', ''], ['https://kineticnight.com/', ''], ['http://www.pbs.up.pt', ''], ['http://www.pbs.up.pt', ''], ['http://www.pbs.up.pt', '']],
        "Fashion":[['https://kineticnight.com/', ''], ['https://kineticnight.com/', ''], ['http://counterclimate.converse.com/', ''], ['https://kineticnight.com/', ''], ['https://kineticnight.com/', '']],
        "Music&Sound":[['https://lilkleine.nl', ''], ['https://fabricofthenation.com/intro', ''], ['http://www.because-recollection.com', ''], ['http://www.because-recollection.com', ''], ['https://lilkleine.nl', '']],
        "E-Commerce":[['http://lummacups.com', ''], ['http://lummacups.com', ''], ['http://lummacups.com', ''], ['https://verholy.com/en/', ''], ['http://lummacups.com', '']],
        "Hotel/Restaurant":[['https://visitevirtuelle.avoriaz.com', ''], ['https://shomabazaar.com', ''], ['https://visitevirtuelle.avoriaz.com', ''], ['https://visitevirtuelle.avoriaz.com', ''], ['https://visitevirtuelle.avoriaz.com', '']],
        "Film&TV":[['https://analogdigital.tv/', ''], ['https://analogdigital.tv/', ''], ['http://swissarmyman.com/', ''], ['https://andreaspsaltis.com/', ''], ['https://analogdigital.tv/', '']],
        "Food&Drink":[['https://goodmeat.co/', ''], ['https://www.metaxa.com/', ''], ['https://oishiii.sushiya.ua/page6927365.html', ''], ['https://goodmeat.co/', ''], ['https://goodmeat.co/', '']],
        "Culture&Education":[['http://www.pbs.up.pt', ''], ['https://www.theatredelaville-paris.com', ''], ['http://www.pbs.up.pt', ''], ['http://www.pbs.up.pt', ''], ['http://www.pbs.up.pt', '']],
        "AppStyle":[['',''],['',''],['',''],['',''],['','']],
        "Architecture":[['https://lighthouseaarhus.dk/', ''], ['https://lighthouseaarhus.dk/', ''], ['https://2.collection-wakawaka.world', ''], ['https://verholy.com/en/', ''], ['https://lighthouseaarhus.dk/', '']],
        "Startups":[['https://www.sciencepark.at', ''], ['https://www.sciencepark.at', ''], ['https://www.bling.eu/', ''], ['https://www.bling.eu/', ''], ['https://www.sciencepark.at', '']],
        "Colorful":[['https://lilkleine.nl', ''], ['https://getuniq.me/en/', ''], ['https://oishiii.sushiya.ua/page6927365.html', ''], ['https://mendeleev.me/', ''], ['https://lilkleine.nl', '']]
    }
    design = ["",""]
    usability = ["",""]
    creativity = ["",""]
    content = ["",""]
    developer = ["",""]

    tags=[] #태그들 들어갈 곳.
    is_exist=False
    site_is_exist = False

    #주제 설정
    try:
        #title2 = Title.objects.all() #모든객체 다불러오기           
        current_title = req.POST['username']
    except:
        current_title = ''
        
    finally:
        before_title = get_object_or_404(Title,pk=3) #전에 태그 가져오기

    #select_choice = Title.objects.get(pk=1)
    #select_choice.title = 'hello'

    #주제에 다른 태그 설정
    if current_title in list(tagResult.keys()):
        is_exist = True
        tags=tagResult[current_title]
        title = Title.objects.get(pk=3)
        title.title = current_title
        title.save()
        before_title = get_object_or_404(Title,pk=3)

    else:
        tags=['Tag1','Tag2','Tag3','Tag4','Tag5']
        before_title = get_object_or_404(Title,pk=3)
    
    #title = get_object_or_404(Title,pk=1)

    try:
        select_tag = req.POST['tag']
    except:
        select_tag = 'none'
    else:
        if not select_tag in ['Tag1','Tag2','Tag3','Tag4','Tag5']:
            tags=tagResult[before_title.title]
            urlList = url_result[select_tag]
            site_is_exist=True
            design = urlList[0]
            usability = urlList[1]
            creativity = urlList[2]
            content = urlList[3]
            developer = urlList[4]
        else:
            pass

        

    context = {
    'name': before_title,
    'is_exist': is_exist,
    'site_is_exist' : site_is_exist,
    'tag1':tags[0],
    'tag2':tags[1],
    'tag3':tags[2],
    'tag4':tags[3],
    'tag5':tags[4],
    'designUrl':design[0],
    'designImg':design[1],
    'usabilityUrl':usability[0],
    'usabilityImg':usability[1],
    'creativtyUrl':creativity[0],
    'creativtyImg':creativity[1],
    'contentUrl':content[0],
    'contentImg':content[1],
    'developerUrl':developer[0],
    'developerImg':developer[1]

    
    }
    return render(req, 'index.html', context)
'''