const report_list = {};

const reportInit = () => {
  const report_msg = [
    "[**SECRET_CONTENT**]",
    "[**SECRET_CONTENT**]",
    "[**SECRET_CONTENT**]",
    "[**SECRET_CONTENT**]",
    "[**SECRET_CONTENT**]",
    "[**SECRET_CONTENT**]",
    "[**SECRET_CONTENT**]",
  ];
  for (let i = 0; i < report_msg.length; i++) {
    report_list[i] = {
      id: i,
      type: "report",
      group: i < 3 ? "admin" : "super_admin",
      msg: report_msg[i],
      time: new Date().getTime(),
    };
  }
};


const getReportList = () => {
  const allReportList = JSON.parse(JSON.stringify(report_list));
// 이 방법을 사용하면 원본 report_list 객체와 독립적인 복사본이 생성되어 참조 없이 객체를 복사할 수 있습니다.
//   const allReportList = report_list; 이러면 독립적인 복사본이 안됨..
  console.log(allReportList);
  for (let report in allReportList) {
    if (allReportList[report].group == "super_admin") {
      allReportList[report].msg = "Access Denied";
    }
  }
  return allReportList;
};

const getReport = (report_id) => {
  let reportData = JSON.parse(JSON.stringify(report_list));
  try {
    return reportData[report_id];
  } catch (e) {
    return {};
  }
};

reportInit();
getReportList();
getReport();