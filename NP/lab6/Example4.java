package com.url.demo;

import java.awt.Graphics;
import javax.swing.JApplet;
import java.net.*;

public class PrintHTMLApplet extends JApplet {
    private URL url = null;
    String strURL = "http://www.chdu.edu.ua";
    if (args.length > 1)
            strURL = args[1];
    public void paint(Graphics g) {
        int timer = 0;
        g.drawString("Завантаження сторінки", 10, 10);
        try {
            for (; timer < 30; ++timer) {
                g.drawString(".", 10 + timer * 5, 25);
                Thread.sleep(100);
            }
            url = new URL(getURL());
            getAppletContext().showDocument(url, "_blank");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}