package com.itheima.reggie.controller;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;


public class RequestUtils {

    public static String sendPost(String url,JSONObject body) {
                RestTemplate restTemplate = new RestTemplate();
        // 设置headers
                HttpHeaders headers = new HttpHeaders();
                headers.add("Content-Type","application/json");

        //设置请求实体
                HttpEntity<String> requestEntity = new HttpEntity<String>(JSON.toJSONString(body), headers);
                try {
                    // 发送请求
                    ResponseEntity<String> response = restTemplate.postForEntity(url, requestEntity, String.class);
                    return response.getBody();
                } catch (Exception e) {
                    return e.getMessage();
                }
    }

}
