package com.itheima.reggie.controller;

import java.util.ArrayList;
import java.util.HashMap;

public class DataStore {

    public static HashMap get_group_name_code(){

        HashMap<String,String> group_name_code= new HashMap<String,String>();
        group_name_code.put("JHU录取群","R:123");
        group_name_code.put("学院群","R:345");
        return group_name_code;

    }




    public static ArrayList get_group_can_in(){
        ArrayList group_can_in = new ArrayList();
        return group_can_in;
    }
}
