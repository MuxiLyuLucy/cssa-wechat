package com.itheima.reggie.entity;

import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.annotation.TableField;
import lombok.Data;
import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * 员工实体
 */
@Data
public class Employee implements Serializable {

    private Long id;

    private String uid = "NA";

    private String email = "NA";

    private String college = "NA";

    private String status = "NA";

    private String block = "NA";

    private String stugpgphd = "NA";

    private String question = "NA";

    private String trynum = "NA";

    private String vermailcode = "NA";

    private String vermaitf = "NA";

    private String groupcanin = "NA";

    private String grouphadin = "NA";


}
/**
 * private String question
 *
 * 0_0 初始值，
 *
 */