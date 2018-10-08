package sel;

/*
 * ver.   1.0
 * subjt. using json api for targeting gates 
 * langs. python
 * maker. ray na
 * group. exciting
 * dates. 2018. 08. 20.
 *  
 */

import java.net.URL;
import java.util.List;
import org.openqa.selenium.*;
import org.openqa.selenium.By.ByName;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

public class sel {
	
	public static void main(String[] args) {
		
		// Request to Java, Setting to Property for Java Selenium 
		System.setProperty("webdriver.chrome.driver", "/Applications/Google Chrome.app/Contents/MacOS/chromedriver");
		
		
		// 1. setting your URL
		String url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%83%9D%EB%B0%B0%EC%A1%B0%ED%9A%8C#";
		
		// 2. making your web driver consider to your web browser 
		WebDriver driver = new ChromeDriver();
		
        // 3. your url give to driver
		driver.get(url);
        
        // 4. for example, your delivery sevice store name & order numbers
        String deliv_name = "롯데택배";
        String deliv_nums = "229568411241";
        
        // 5. web element traker ... (need to your customizing)
        WebElement taeckBae_name = driver.findElement(By.cssSelector("select._select"));
        taeckBae_name.sendKeys(deliv_name.toString());
        
        WebElement taeckBae_nums = driver.findElement(By.cssSelector("input#numb._input.in_bx"));
        taeckBae_nums.sendKeys(deliv_nums.toString());
        
        WebElement taeckBae_submit = driver.findElement(By.cssSelector("input._submit.sc_btn"));
        taeckBae_submit.click();
            
        WebElement table_data = driver.findElement(By.cssSelector("#_doorToDoor > div._output > div.rsult_box > dl > dd.blind"));
        System.out.println(table_data.getText());
                    
        // 6. Page Load Process ...
        (new WebDriverWait(driver, 10)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getTitle().toLowerCase().startsWith("라면");
            }
        });

        // 7. Driver quit 
        driver.quit();		
		
	}
	
}
