
--
-- Database: `meetme`
--

-- --------------------------------------------------------
CREATE TABLE meetme (
    confno char(80) DEFAULT '0' NOT NULL,
    -- Web booking id for the conference
    bookId char(50) NULL,
    -- Must set schedule=yes in meetme.conf to use starttime and endtime
    starttime datetime NULL,
    endtime datetime NULL,
    -- PIN to enter the conference, if any
    pin char(30) NULL,
    -- Options to associate with normal users of the conference
    opts char(100) NULL,
    -- PIN to enter the conference as an administrator, if any
    adminpin char(30) NULL,
    -- Options to associate with administrator users of the conference
    adminopts char(100) NULL,
    -- Current count of conference participants
    members integer DEFAULT 0 NOT NULL,
    -- Maximum conference participants allowed concurrently
    maxusers integer DEFAULT 0 NOT NULL,
    -- Recording of the conference, if any
    recordingfilename char(255) NULL,
    -- File format of the conference recording, if any
    recordingformat char(10) NULL,
    PRIMARY KEY (confno, starttime)
);

INSERT INTO meetme (confno,pin,adminpin,members,starttime,endtime) VALUES ("500O","1234","2345","0","2009-09-24 19:00","2009-09-24 20:00");


--
-- Table structure for table `booking`
--


CREATE TABLE IF NOT EXISTS `booking` (
  `bookId` int(10) unsigned NOT NULL auto_increment,
  `clientId` int(10) unsigned default '0',
  `confno` varchar(30) default '0',
  `pin` varchar(30) NOT NULL default '0',
  `adminpin` varchar(30) NOT NULL default '0',
  `starttime` datetime NOT NULL default '0000-00-00 00:00:00',
  `endtime` datetime NOT NULL default '0000-00-00 00:00:00',
  `dateReq` datetime NOT NULL default '0000-00-00 00:00:00',
  `dateMod` datetime NOT NULL default '0000-00-00 00:00:00',
  `maxUser` varchar(30) NOT NULL default '10',
  `status` varchar(30) NOT NULL default 'A',
  `confOwner` varchar(30) NOT NULL default '',
  `confDesc` varchar(100) NOT NULL default '',
  `adminopts` varchar(10) NOT NULL default '',
  `opts` varchar(10) NOT NULL default '',
  `sequenceNo` int(10) unsigned default '0',
  `recurInterval` int(10) unsigned default '0',
  PRIMARY KEY  (`bookId`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=145 ;

--
-- Dumping data for table `booking`
--


-- --------------------------------------------------------

--
-- Table structure for table `cdr`
--

CREATE TABLE IF NOT EXISTS `cdr` (
  `bookId` int(11) default NULL,
  `duration` varchar(12) default NULL,
  `CIDnum` varchar(32) default NULL,
  `CIDname` varchar(32) default NULL,
  `jointime` datetime default NULL,
  `leavetime` timestamp NULL default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cdr`
--


-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE IF NOT EXISTS `notifications` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL default '0',
  `book_id` int(11) NOT NULL default '0',
  `ntype` char(10) default NULL,
  `ndate` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `notifications`
--


-- --------------------------------------------------------

--
-- Table structure for table `participants`
--

CREATE TABLE IF NOT EXISTS `participants` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL default '0',
  `book_id` int(10) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=782 ;

--
-- Dumping data for table `participants`
--


-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL auto_increment,
  `email` varchar(100) NOT NULL default '',
  `password` varchar(25) default NULL,
  `first_name` varchar(50) default NULL,
  `last_name` varchar(50) default NULL,
  `telephone` varchar(15) default NULL,
  `admin` varchar(5) NOT NULL default 'User',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;




--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `first_name`, `last_name`, `telephone`, `admin`) VALUES
(20, 'wmm@localhost', 'wmmpw', 'Web', 'MeetMe', '1234', 'Admin');



