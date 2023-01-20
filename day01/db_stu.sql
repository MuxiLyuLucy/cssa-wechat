/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50728
Source Host           : localhost:3306
Source Database       : reggie

Target Server Type    : MYSQL
Target Server Version : 50728
File Encoding         : 65001

Date: 2021-07-23 10:41:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_info
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `id` bigint(20) NOT NULL COMMENT '主键',
  `uid` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '用户id',
  `email` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '邮箱',
  `college` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '学院',
  `status` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '身份(1:在校;2:毕业;3.拿到offer未入学4.在校gap)',
  `block` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '屏蔽(0:不是; 1:是)',
  `stugpgphd` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '本硕博(ug,pg,phd)',
  `question` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '所处题目（比如1.1，2.4，4.6）',
  `trynum` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '尝试次数（防恶意）',
  `vermailcode` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '邮箱验证码',
  `vermaitf` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '邮箱验证通过与否 (0未通过1通过）',
  `groupcanin` varchar(400) COLLATE utf8_bin NOT NULL COMMENT '可以加入的群',
  `grouphadin` varchar(400) COLLATE utf8_bin NOT NULL COMMENT '已经加入的群',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `idx_uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='用户表';

-- -- ----------------------------
-- -- Records of tb_info
-- -- ----------------------------
-- INSERT INTO `tb_info` VALUES ('1417414526093082626', '1417012167126876162', '小明', '1', '13812345678', null, null, null, null, null, null, '昌平区金燕龙办公楼', '公司', '1', '2021-07-20 17:22:12', '2021-07-20 17:26:33', '1417012167126876162', '1417012167126876162', '0');
-- INSERT INTO `tb_info` VALUES ('1417414926166769666', '1417012167126876162', '小李', '1', '13512345678', null, null, null, null, null, null, '测试', '家', '0', '2021-07-20 17:23:47', '2021-07-20 17:23:47', '1417012167126876162', '1417012167126876162', '0');

