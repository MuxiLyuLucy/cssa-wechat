package com.itheima.reggie.controller;

import com.alibaba.fastjson.JSONObject;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.itheima.reggie.common.R;
import com.itheima.reggie.entity.Employee;
import com.itheima.reggie.service.EmployeeService;
import lombok.Synchronized;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.task.SyncTaskExecutor;
import org.springframework.util.DigestUtils;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.itheima.reggie.controller.UtilsController;
import com.itheima.reggie.controller.RequestUtils;

import java.util.*;
import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;



@Slf4j
@RestController
//@RequestMapping("/message")
public class EmployeeController {

    @Autowired
    private EmployeeService employeeService;

    /**
     * 员工登录
     * @param request
     * @param employee
     * @return
     */
    @PostMapping("/message")
    public R<Employee> login(HttpServletRequest request,@RequestBody String employee) {

        // prase成json进行解析
        JSONObject json = (JSONObject) JSONObject.parse(employee);
        JSONObject json2 = (JSONObject) json.get("data");

        // 获取关键字段
        String re_Payload = (String) json2.get("payload");
        String chat_id_reply = (String) json2.get("chatId");

        // System.out.print(json2);

        // 参数注入对象
        Employee employee_a = new Employee();
        employee_a.setUid((String) json2.get("contactId"));

        // 研究数据库是否存在数据
        LambdaQueryWrapper<Employee> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.eq(Employee::getUid, employee_a.getUid());
        Employee emp = employeeService.getOne(queryWrapper);

        // 未查询到：存储员工信息
        if (emp == null) {
            log.info("新增员工，员工信息：{}", employee_a.toString());
            // 设置初始题号
            employee_a.setQuestion("0_0");
            // 存储员工信息
            employeeService.save(employee_a);
            // 发送欢迎语
            ques_0_0_pre(employee_a, chat_id_reply);
            return R.error("账号已添加");
        }

        // 查询到：寻找相对应的题号
        String emp_question = emp.getQuestion();


        // 验证身份后
        if (emp_question.equals("0_0")){
            ques_0_0(employeeService,emp,chat_id_reply);
        }
        // 询问邮箱
        else if (emp_question.equals("1_1")) {
            ques_1_1(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 回答邮箱，发送验证码
        else if (emp_question.equals("2_0")) {
            ques_2_0(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 回答验证码
        else if (emp_question.equals("2_1")) {
            ques_2_1(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 拉群
        else if (emp_question.equals("3_1")) {
            ques_3_1(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 拉入新生群，询问本硕
        else if (emp_question.equals("4_0")) {
            ques_4_0(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 获取本硕，询问学院
        else if (emp_question.equals("4_1")) {
            ques_4_1(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 获取学院，显示可以加入的群聊
        else if (emp_question.equals("4_2")) {
            ques_4_2(employeeService,emp,re_Payload,chat_id_reply);
        }
        // 获取加入群聊需求，加入群聊
        else if (emp_question.equals("4_3")) {
            ques_4_3(employeeService,emp,re_Payload,chat_id_reply);
        }



        return R.error("账号已禁用:"+emp_question);
    }



    /**
     * 0_0 pre 发送欢迎语
     */
    public static void ques_0_0_pre(Employee emp, String chat_id_reply){
        String send_txt = "Hihi，同学你好呀! 我是JHU学联加群小助手，很高兴为您服务。\n\n目前小助手为初始阶段，仅为23fall新生提供服务。学联目前为已有JHU邮箱的同学提供新生群，学院群以及校区群。确认系统稳定后，学联日后会增加更多微信群（公寓群，兴趣群，租房/二手群等）。\n\n若您未获取JHU邮箱后缀，您可以通过EDU后缀的邮箱进入录取群。若遇到问题，请添加学联小助手微信咨询（wx：johnshopkinscssa）\n \n如果您准备好加群了，回答大写“A”以继续";
        response_msg(send_txt,chat_id_reply);
    }

    /**
     * 检查0_0  发送是否有edu邮箱
     */
    public static void ques_0_0(EmployeeService employeeService, Employee emp, String chat_id_reply){
        String send_txt = "请选择您的邮箱种类：\nA.JHU邮箱 \nB.非JHU的EDU后缀邮箱 \nC.无EDU邮箱";
        response_msg(send_txt,chat_id_reply);
//        ***测试发送消息和加群功能***
//        System.out.print("respond测试1-----通过");
//        response_groupadd();
//        System.out.print("respond测试2-----通过");
//        response_msg(send_txt);
//        System.out.print("respond测试3-----通过");
        // 更新
        emp.setQuestion("1_1");
        // 测试的时候修改
        // emp.setQuestion("0_0");

        employeeService.updateById(emp);
    }

    /**
     * 检查1_1  接受存储edu信息：(1) 若A，则发送验证码；(2) 若B，则发送加群信息。(3) 若c联系管理员
     */
    public static void ques_1_1(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
        // 若A，则询问邮箱
        if (re_Payload.equals("A")){
            String send_txt = "请输入您的JHU邮箱： \n\n *后缀为jh.edu/jhu.edu/jhmi.edu";
            // 更新
            emp.setQuestion("2_0");
            emp.setStatus("em_jhu");
            employeeService.updateById(emp);

            response_msg(send_txt,chat_id_reply);
        }
        // 若B，则询问邮箱
        if (re_Payload.equals("B")){
            String send_txt = "请输入您的EDU后缀邮箱：";
            // 更新
            emp.setStatus("em_edu");
            emp.setQuestion("2_0");
            employeeService.updateById(emp);

            response_msg(send_txt,chat_id_reply);
        }
        // 若C，则发送寻找管理员

        if (re_Payload.equals("C")){
            String send_txt = "自动系统目前并不能帮您加群。\n\n若您与JHU系统有关，但没有邮箱，请您添加学联小助手微信号‘johnshopkinscssa’，进行人工验证核查。";
            // 更新
            emp.setStatus("em_noedu");
            emp.setQuestion("0_0");
            employeeService.updateById(emp);

            response_msg(send_txt,chat_id_reply);
        }

    }

    /**
     * 检查2_0  接受对方输入的邮箱
     */
    public static void ques_2_0(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
            if((emp.getStatus().equals("em_jhu"))&&(!re_Payload.contains("jh"))){
                response_msg("您输入的邮箱并非是JHU邮箱，请输入正确的JHU邮箱",chat_id_reply);
                ques_0_0(employeeService,emp, chat_id_reply);
                return;
            }
            if((emp.getStatus().equals("em_edu"))&&(!re_Payload.contains("edu"))){
                response_msg("您输入的邮箱并非是edu邮箱，请输入正确的edu邮箱",chat_id_reply);
                ques_0_0(employeeService,emp, chat_id_reply);
                return;
            }

            // 对方输入了邮箱
            String send_txt = "验证码已发送，请您查看邮件。（可能在垃圾信箱）\n\n请回复x位数验证码：";
            // 发送验证码

            // 更新
            emp.setEmail(re_Payload);
            emp.setVermailcode("123");
            emp.setQuestion("2_1");
            employeeService.updateById(emp);

            response_msg(send_txt,chat_id_reply);
    }



    /**
     * 检查2_1  回答了验证码，检验验证码是否正确；(A)正确，拉群；(B)错误，询问是否再发送。
     */
    public static void ques_2_1(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply) {
        // 获取验证码信息
        String code_from_db = emp.getVermailcode();
        // 分析Jhu 还是 edu
        String stu_status = emp.getStatus();
        String send_txt;
        // 加入原有
        String pre_str = emp.getGroupcanin();
        List<String> group_could_in = new ArrayList<String>();
        if (pre_str.equals("NA")) {
            int a = 1;
        }else {
            String str[] = pre_str.split(",");
            group_could_in = Stream.of(str).collect(Collectors.toCollection(ArrayList::new));
        }

        if (re_Payload.equals("123")) {
            if (stu_status.equals("em_jhu")) {
                emp.setStatus("emv_jhu");
                send_txt = "您可以加入以下群聊：\n\nA. JHU2023新生群";
                // 添加新群
                group_could_in.add("_23NewStu");
                emp.setQuestion("4_0");

                response_msg(send_txt,chat_id_reply);
            }
            if (stu_status.equals("em_edu")) {
                emp.setStatus("emv_edu");
                send_txt = "您可以加入以下群聊：\n\nA. JHU2023录取群";
                // 添加新群
                group_could_in.add("_23offer");
                emp.setQuestion("3_1");

                response_msg(send_txt,chat_id_reply);
            }
            // 更新
                //转字符串
            String group_could_in_str = StringUtils.join(group_could_in,",");
            emp.setGroupcanin(group_could_in_str);
                //其他更新
            employeeService.updateById(emp);

        } else { // 验证码错误，
            send_txt = "验证码错误，请重新输入邮箱：";

            response_msg(send_txt,chat_id_reply);

            // 返回询问邮箱
            ques_0_0(employeeService, emp, chat_id_reply);
        }

    }

    /**
     * 检查3_1  无邮箱回答了拉群需求，则拉群
     */
    public static void ques_3_1(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
        // 拉群
        String send_txt;

        if (re_Payload.equals("A")){
                send_txt = "已拉您入录取群。\n\n*因代写/广告/换汇诈骗等因素，录取群会在2023Fall开学前解散。\n\n**若您在未来成功获取JHU邮箱，请返回重新验证，加入JHU学生专属社群。";
                // 拉群
                String wx_id = emp.getUid();
                response_groupadd("R:10799942872593752",wx_id);
                response_msg(send_txt,chat_id_reply);
            // 更新
            emp.setQuestion("0_0");
            employeeService.updateById(emp);
        }

    }

    /**
     * 检查4_0  jhu后缀 拉入新生群
     */
    public static void ques_4_0(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
        // 拉群
        String send_txt;

        if (re_Payload.equals("A")){
            send_txt = "已拉您入新生群。接下来我们会问您一系列问题，以方便邀请您进入其他群。\n\n请问您是: \nA.本科\nB.DC校区硕士\nC.Bal校区硕士\nD.博士 \n\n *DC校区的硕士项目包括SAIS, 部分Carey，以及除Biotech和Film and Media之外的AAP Program。本科，博士，以及其余的硕士项目均在巴尔的摩。";
            // 拉群
            String wx_id = emp.getUid();
            response_groupadd("R:10769365486412508",wx_id);
            response_msg(send_txt,chat_id_reply);
            // 更新
            emp.setQuestion("4_1");
            employeeService.updateById(emp);
        }

    }


    /**
     * 检查4_1  询问本科硕士后的返回值
     */
    public static void ques_4_1(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
        // 根据不同情况分配群
        String send_txt;
        // 加入原有
        String pre_str = emp.getGroupcanin();
        List<String> group_could_in = new ArrayList<String>();
        if (pre_str.equals("NA")) {
            int a = 1;
        }else {
            String[] str = pre_str.split(",");
            group_could_in = Stream.of(str).collect(Collectors.toCollection(ArrayList::new));
        }


        if (re_Payload.equals("A")){
            // 更新
            group_could_in.add("_23Cof2027");
            emp.setQuestion("4_2");
            emp.setStugpgphd("_23Cof2027");
        }

        else if (re_Payload.equals("B")){
            // 更新
            group_could_in.add("_23DC");
            emp.setQuestion("4_2");
            emp.setStugpgphd("_23DC");
        }

        else if (re_Payload.equals("C")){
            // 更新
            group_could_in.add("_23Bal");
            emp.setQuestion("4_2");
            emp.setStugpgphd("_23Bal");
        }

        else if (re_Payload.equals("D")){
            // 更新
            group_could_in.add("_23Bal");
            group_could_in.add("_23PHD");
            emp.setQuestion("4_2");
            emp.setStugpgphd("phd");
        } else{
            return;
        }
            // 更新
            //转字符串
            String group_could_in_str = StringUtils.join(group_could_in,",");
            emp.setGroupcanin(group_could_in_str);
            // 其他更新
            employeeService.updateById(emp);

        send_txt = "请问您是：\nA.Whiting工学院\nB.Krieger文理学院\nC.Peabody音乐学院\nD.Carey商学院\nE.SOE教育学院\nF.SAIS国际关系学院\nG.East Baltimore三院 (Bloomberg, Nursing, Medicine)";
        response_msg(send_txt,chat_id_reply);

    }

    /**
     * 检查4_2 根据学院，记录学院，显示结果
     */

    public static void ques_4_2(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
        // 根据不同情况分配群
        String send_txt;
        // 加入原有
        String pre_str = emp.getGroupcanin();
        List<String> group_could_in = new ArrayList<String>();
        if (pre_str.equals("NA")) {
            int a = 1;
        }else {
            String str[] = pre_str.split(",");
            group_could_in = Stream.of(str).collect(Collectors.toCollection(ArrayList::new));
        }


        if (re_Payload.equals("A")){
            group_could_in.add("_23Whiting");
            emp.setCollege("_23Whiting");
        }

        else if (re_Payload.equals("B")){
            group_could_in.add("_23Kriger");
            emp.setCollege("_23Kriger");
        }

        else if (re_Payload.equals("C")){
            group_could_in.add("_23Peabody");
            emp.setCollege("_23Peabody");
        }

        else if (re_Payload.equals("D")) {
            group_could_in.add("_23Carey");
            emp.setCollege("_23Carey");
        }

        else if (re_Payload.equals("E")) {
            group_could_in.add("_23SOE");
            emp.setCollege("_23SOE");
        }

        else if (re_Payload.equals("F")) {
            group_could_in.add("_23SAIS");
            emp.setCollege("_23SAIS");
        }

        else if (re_Payload.equals("G")){
            group_could_in.add("_23EastBal");
            emp.setCollege("_23EastBal");

        } else{
            return;
        }
        // 更新
        // 去重
        group_could_in = new ArrayList<String>(new HashSet<String>(group_could_in));
        //转字符串
        String group_could_in_str = StringUtils.join(group_could_in,",");
        emp.setGroupcanin(group_could_in_str);


        // 其他更新
        emp.setQuestion("4_3");
        employeeService.updateById(emp);

        // 通过数据库raw_str和分析函数获取可加入群聊字符串
        String db_raw_group_could_in_str = emp.getGroupcanin();
        String return_group_could_in_str = show_group_could_in(db_raw_group_could_in_str);

        send_txt = return_group_could_in_str;
        response_msg(send_txt,chat_id_reply);

    }


    /**
     * 检查4_3 根据学生加群意愿，加入群聊，再次显示可加入群聊页面
     */
    public static void ques_4_3(EmployeeService employeeService, Employee emp,String re_Payload, String chat_id_reply){
        // 先分析其回复的字母是想加入哪个群聊
        String send_txt;
        // 通过数据库raw_str分析他可加入群聊的code-list
        String db_raw_group_could_in_str = emp.getGroupcanin();
        ArrayList group_could_in_code= show_group_could_in_code(db_raw_group_could_in_str);

        // 观察区间是否大于等于0且小于arraylist长度。
        if (isInteger(re_Payload)){
            // 根据代码拉群
            int want_group_id = Integer.parseInt(re_Payload);

            if ((want_group_id <= group_could_in_code.size()) && (want_group_id > 0)) {
                // 拉群
                String wx_id = emp.getUid();
                response_groupadd((String) group_could_in_code.get(want_group_id - 1),wx_id);
            }else{
                response_msg("回复错误，请回复正确的数字。",chat_id_reply);
                return;
            }
        }

        else{
            // 若回复错字母
            response_msg("回复错误，请回复数字。",chat_id_reply);
            return;
        }

        // 其他更新
        emp.setQuestion("4_3");
        employeeService.updateById(emp);

        // 通过数据库raw_str和分析函数获取可加入群聊字符串
        String return_group_could_in_str = show_group_could_in(db_raw_group_could_in_str);

        send_txt = "已邀请您加入群聊。"+return_group_could_in_str;
        response_msg(send_txt,chat_id_reply);

    }


    /**
     * 工具类 根据字符串显示可加入的群聊
     */

    public static String show_group_could_in(String db_raw_group_could_in_str){
        // 分割字符串并取出相应的群id，根据id查找群名，生成群名list
        List<String> group_could_in = new ArrayList<String>();
        if (db_raw_group_could_in_str.equals("NA")) {
            int a = 1;
        }else {
            String str[] = db_raw_group_could_in_str.split(",");
            group_could_in = Stream.of(str).collect(Collectors.toCollection(ArrayList::new));
        }
        // 查找遍历和生成
        HashMap college_id_name = create_college_id_name_hash();
        String qunming_list_ans = "回复数字即可加入以下群聊:   \n";
        int count_order = 0;
        for(String tmp:group_could_in){
            count_order++;
            qunming_list_ans = qunming_list_ans + String.valueOf(count_order) + "." + college_id_name.get(tmp) + "\n";
        }

        // 遍历群名list生成字符串
        return qunming_list_ans;
    }

    /**
     * 工具类 根据字符串显示可加入的群聊
     */

    public static ArrayList show_group_could_in_code(String db_raw_group_could_in_str){
        // 创建code list.
        ArrayList group_could_in_code = new ArrayList();

        // 分割字符串并取出相应的群id，根据id查找群code,生成code list.
        List<String> group_could_in = new ArrayList<String>();
        if (db_raw_group_could_in_str.equals("NA")) {
            int a = 1;
        }else {
            String str[] = db_raw_group_could_in_str.split(",");
            group_could_in = Stream.of(str).collect(Collectors.toCollection(ArrayList::new));
        }
        HashMap college_id_code = create_college_id_code_hash();
        for(String tmp:group_could_in){
            group_could_in_code.add(college_id_code.get(tmp));
        }
        // 返回可加群code list
        return group_could_in_code;
    }


    /**
     * 数据类 hashmap -> key:学院代码 value:学院群号码
     */

    public static HashMap create_college_id_code_hash(){
        HashMap<String,String> college_id_code = new HashMap();
        college_id_code.put("_23offer","R:10799942872593752");
        college_id_code.put("_23NewStu","R:10769365486412508");
        college_id_code.put("_23DC","R:10886124391200410");
        college_id_code.put("_23Bal","R:10724434264269354");
        college_id_code.put("_23Cof2027","R:10945711955814589");
        college_id_code.put("_23Whiting","R:10912690677834683");
        college_id_code.put("_23Kriger","R:10802090643191755");
        college_id_code.put("_23Peabody","R:10757964468350095");
        college_id_code.put("_23Carey","R:10722131315561425");
        college_id_code.put("_23SOE","R:10759955487367415");
        college_id_code.put("_23SAIS","R:10934526223913929");
        college_id_code.put("_23EastBal","R:10895004953815983");
        college_id_code.put("_23PHD","R:10720999534523155");

        return college_id_code;

    }

    /**
     * 数据类 hashmap -> key:学院代码 value:学院群号码
     */

    public static HashMap create_college_id_name_hash(){
        HashMap<String,String> college_id_name = new HashMap();
        college_id_name.put("_23offer","JHU2023录取群");
        college_id_name.put("_23NewStu","JHU2023新生群");
        college_id_name.put("_23DC","JHU23在DC小伙伴");
        college_id_name.put("_23Bal","JHU23在Bal小伙伴");
        college_id_name.put("_23Cof2027","JHU Class of 2027");
        college_id_name.put("_23Whiting","JHU工学院 23-24");
        college_id_name.put("_23Kriger","JHU文理学院 23-24");
        college_id_name.put("_23Peabody","JHU音乐学院 23-24");
        college_id_name.put("_23Carey","JHU商学院 23-24");
        college_id_name.put("_23SOE","JHU教育学院 23-24");
        college_id_name.put("_23SAIS","JHU国际关系学院 23-24");
        college_id_name.put("_23EastBal","JHU医学三院 23-24");
        college_id_name.put("_23PHD","JHU PhD群");


        return college_id_name;

    }


    /**
     * 工具类 response：回话,返回txt
     */
    public static void response_msg(String msg, String chat_id_reply){
        String url = "https://ex-api.botorange.com/message/send";
//        //封装消息
        HashMap text = new HashMap();
        text.put("text",msg);
//        //参数

        JSONObject params = new JSONObject();
        params.put("chatId",chat_id_reply);
        params.put("token","62c66439bacbe0a74279a6ff");
        params.put("messageType",0);
        params.put("payload",text);

        String result = RequestUtils.sendPost(url,params);
    }

    /**
     * 工具类 response:加群,返回txt
     */
    public static void response_groupadd(String r_code, String wx_id){
        String url = "https://ex-api.botorange.com/room/addMember";
        //参数

        JSONObject params = new JSONObject();
        params.put("token","62c66439bacbe0a74279a6ff");
        params.put("botUserId","jhuJiaQunXiaoZhuShou");
        params.put("contactWxid",wx_id);
        params.put("roomWxid",r_code);

        String result = RequestUtils.sendPost(url,params);
    }

    /**
     * 工具类 检查是否为数字
     */
    public static boolean isInteger(String str) {
        Pattern pattern = Pattern.compile("^[-\\+]?[\\d]*$");
        return pattern.matcher(str).matches();
    }

}


