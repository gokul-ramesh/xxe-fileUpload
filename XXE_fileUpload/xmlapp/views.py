from django.shortcuts import render, redirect
from .models import XMLData
from xml.etree import ElementTree as ET
from lxml import etree
import traceback

def upload_xml(request):
    if request.method == 'POST':
        xml_file = request.FILES['xml_file']
        try:       
            parser = etree.XMLParser(resolve_entities=True, no_network=False) 
            tree = etree.parse(xml_file, parser=parser)
            root = tree.getroot()
            title = root.find('.//title').text
            xxe = root.find('.//xxe').text
            print(xxe)
        except etree.XMLSyntaxError as e:
            title = str(e)
        except Exception as e:
            title = "Error XML!!"
        
        xml_data = XMLData(title=title, xml_file=xml_file)
        xml_data.save()

        return redirect('display_xml', xml_data.id)

    return render(request, 'upload_xml.html')

def display_xml(request, xml_id):
    xml_data = XMLData.objects.get(id=xml_id)
    return render(request, 'display_xml.html', {'xml_data': xml_data})
