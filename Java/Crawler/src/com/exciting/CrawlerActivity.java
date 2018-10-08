package com.exciting;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.Charset;
import java.util.Iterator;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.HttpResponseException;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


class Crawler {
	
	String url = "";
	int startNum = 0;
	int endNum = 0;
	String crawlName = "";
	String crawlContents = "";
	
	CrawlerActivity c;
	
	public void crawlerOptions() {
		
		c = new CrawlerActivity();
		
		switch (c.Gu.toString()) {
		case "중랑구" :
			url = "http://jungnang.webstore.kr/html/040100_zoom.php?no=";
			startNum = 71;
			endNum = 7843;
			crawlName = "tbody tr th";
			crawlContents = "tbody tr td";
			break;
			
		case "용산구" :
			url = "http://yongsan-toy.or.kr/html/sub/index.php?pno=03010201&mode=view&itemcode=";
			break;

		case "강북구" :
			break;
		
		case "도봉구" :
			break;
			
		case "은평구" :
			break;

		case "서대문구" :
			break;

		case "마포구" :
			break;

		case "종로구" :
			break;
			
		case "중구" :
			break;

		}
	}
}

public class CrawlerActivity {

	public String Gu = "중랑구";
	
	public static void main(String args[]) {
		Crawler c = new Crawler();			
		
//		System.out.println(c.crawlerOptions.);
//		HttpClient httpClient = new DefaultHttpClient();
//		
//		for (int i = c.startNum; i <= c.endNum; i++) {
//			
//			HttpGet httpget = new HttpGet(c.url.toString() + i);
//			
//			try {
//				httpClient.execute(httpget, new BasicResponseHandler() {
//
//				@Override
//				public String handleResponse(HttpResponse response) throws HttpResponseException, IOException {
//					
//					String res = new String(super.handleResponse(response));
//					byte [] utf8 = res.getBytes(Charset.forName("euc-kr"));				
//					Document doc = Jsoup.parse(res);
//					Elements rows1 = doc.select(c.crawlName.toString());
//					Elements rows2 = doc.select(c.crawlContents.toString());
////					String[] items = new String[] { "제목" };
//	//
////					for (Element row : rows) {
////						Iterator<Element> iterElem = row.getElementsByTag("td").iterator();
////						StringBuilder builder = new StringBuilder();
//	//
////						for (String item : items) {
////							builder.append(item + ": " + iterElem.next().text() + "\t");
////						}
//
////					System.out.println(builder.toString());
//					System.out.println( rows1.text().toString() );
//					System.out.println( rows2.text().toString() );
////					}
//					return res;
//				}
//				});
//			} catch (ClientProtocolException e) {
//				e.printStackTrace();
//			} catch (IOException e) {
//				e.printStackTrace();
//			}
//		}
	}
}
