import requests
from bs4 import BeautifulSoup
import pandas as pd

#for length of data
x = requests.get("https://merolagani.com/Floorsheet.aspx")
soup = BeautifulSoup(x.text,'html.parser')
temp = soup.find("span",{"class":"hidden-xs"}).text
temp_d = temp.split(":")
print(temp_d)
dataLength = int(temp_d[1].strip(']'))
print(f"TOTAL NUMBER OF PAGES:{dataLength}")

# empty list
data = []
   
# for getting the header from
# the HTML file
list_header = []

header = soup.find_all("table")[0].find("tr")
  
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  

for i in range(1,dataLength+1):
    print(f"RETRIVING DATA OF PAGE {i}")
    x = requests.post("https://merolagani.com/Floorsheet.aspx",data={
        	"__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": "1LZH3mWxk6I+Gb2kQitSBi9IHWMi2GsxAmySFw+eKO8f1aD2MRWWaOGVSqpVq2BbEQwstM4OlCz8bN0rqwnzK8hIPc83Bw+hpO5z+1m/S0zyz3vVL6LQNmTS9Bpr1WEQRew+8kyX5KxcaRoX+Ch+/QA3rCd8VyhB2cacDOQIdjitJBlfA86l6eqWFWxuG53bGOQyw21PtgiTxiXqWE1ndCMxDD5+Has4Or6Jy8HSSWjpP75zlpDfp9CouBbw9xe09Wg7NjxUo8KO9BiB/gKqZbKPc8XrMg03nJ+OcdMfen+C2g5XoI/IEim0B8XntToE2RbfIobYXhn6vs3ASoL/W4PWm85rva5VHPcGUEslPbL3cvkRSSnEFL1w6+bGxxFzR8lxY8x0Zxrf5V8dV/YSdTi+LxULfFavMb3uSXWLpbz+SKL/ArZD31ZI2LOx6HYlkH2lz9oLwMS4OiUrbHqJ/aS0HVlqsf5u9xDGNXKbQpDGSCmXZwhx5pVUQ8XfsPbzBq2e8rp3sStR256XSNjZzlT/ZIw5QFy5OSGq3DDgZBIj9pqPb3nQGpdZ9vCoNIjUezM/0qTs4ZCOfLPdGniftZ1lKbfgnu5ao3AN558xveOCCW8DZcmKMHLddlsMv1UgkzY/cjnvjRMtPNWk5mIggW5jpIpYooSoyImfPart6WGnPvfcGakXAbPnvtfnwPslf6EpWoz+oi48RrD03CAN40Nk1sj4/37pfwW25CyK8bKAXTmNCJMHciYn/sdXqJuUJAo4J5QuoD4HNPHdjTkIQcf/nptxNcJUqE5Qc9RvlvluRZcDejHPDaTvDIt1RLZmwi8ZeF0A2f61eoEamYqYQ+wRPQmqhlLdirnevVudT1CD9F3uDETgbrV43nawUIt7ZbR0werTIptxbynoHCMkYFz+Ww2owTZ4R5uwplq94nTcorswtTEOVB/jGre4ywZ2vE8pWP0Pxd+cZOjdMihGSFUj+yEPOSToadYpvpy6sFQ/BaL/hoMxE1GrnewnkVLE",
                "__VIEWSTATEGENERATOR": "1F15F17F",
                "__EVENTVALIDATION": "NU3MsIEC9pvVVp2qLwvsLjXavPjTzundjOYQ36M90uyHcyEpf14oaaWI6Nrnl3jjLcz8AHY623gzqEZFevcbg+ptQ26KgZ0HUgg9vnbKbD1V+f19e0sXr9bRZG5hIiv56FbaDVnZOmFFhe+/fy0d57gZwU8tcnR7ZWC6Y7QtVnB9djhL1z9R/0rNN7V06AJXCZmdC4I50VktfJWLm1070iyC4LIbxQkhvh8AOx+n6GVnipmsXN13+FmY3u2ab6ksQAhEottMudCJbsIUvazcPr+HjsgQf7JtSjCkvNOORrCe+d5Kxrqq3zM/Q/6OWnnAobvKq5t5VYtIApnSe28wXoPuQ/4QkE0utYMLYqOKLrNUc5UODYx1w8+rv08kd8wgs6XIf/w6ga9YWN/QhRcN9iYrNQGvlMIUsud2LpZd2iTLBL5tm8/re9lPPwUHVXmcwAiPu/zyh9+RvaWhdyCXQ/4FGjaVzg9sQrrh1ZKKTfkE9uS3++nOn10bGKAiEKMG+1BL51asT5vKu+NurzpAHB4X8/4MkkIFCasL8HkLrSZ6ABk5x2hnfh3wcf/V64lG",
                "ctl00$ASCompany$hdnAutoSuggest": "0",
                "ctl00$ASCompany$txtAutoSuggest": "",
                "ctl00$txtNews": "",
                "ctl00$AutoSuggest1$hdnAutoSuggest": "0",
                "ctl00$AutoSuggest1$txtAutoSuggest": "",
                "ctl00$ContentPlaceHolder1$ASCompanyFilter$hdnAutoSuggest": "0",
                "ctl00$ContentPlaceHolder1$ASCompanyFilter$txtAutoSuggest": "",
                "ctl00$ContentPlaceHolder1$txtBuyerBrokerCodeFilter": "",
                "ctl00$ContentPlaceHolder1$txtSellerBrokerCodeFilter": "",
                "ctl00$ContentPlaceHolder1$txtFloorsheetDateFilter": "",
                "ctl00$ContentPlaceHolder1$PagerControl1$hdnPCID": "PC1",
                "ctl00$ContentPlaceHolder1$PagerControl1$hdnCurrentPage": i,
                "ctl00$ContentPlaceHolder1$PagerControl1$btnPaging": "",
                "ctl00$ContentPlaceHolder1$PagerControl2$hdnPCID": "PC2",
                "ctl00$ContentPlaceHolder1$PagerControl2$hdnCurrentPage": "0"})
    soup = BeautifulSoup(x.text,'html.parser')
    # for getting the data 
    HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
  
    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)
  
# Storing the data into Pandas
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
   
# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv('Floorsheet.csv')
print("YOUR TASK IS COMPLETE PLEASE CHECK FLOOTSHEET.CSV")
