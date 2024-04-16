const fs = require("fs");
const INPUTFILE = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(INPUTFILE).toString().trim().split("\n");

const N = Number(input[0]);
let schedule = [];
for (let i = 0; i < N; i++) {
  var [s, e] = input[i + 1].split(" ").map(Number);
  schedule.push([s, e]);
  //[schedule[i]["s"], schedule[i]["e"]] = input[i + 1].split(" ").map(Number);
}
// console.log(schedule);
// a 끝나는시간 < b 시작시간
// b 중에서 가장 끝나는 시간이 빠른 회의 선택
// 끝나는 시간이 같다면 b 중에서 가장 시작 시간이 빠른 회의 선택

// 다중 조건 정렬
schedule.sort((a, b) => a[1] - b[1] || a[0] - b[0]);

var a_meeting_end, b_meeting_start;
let ans = schedule.reduce((prev, cur, i) => {
  if (i === 0) {
    prev.push(cur);
    a_meeting_end = schedule[i][1];
  } else {
    b_meeting_start = schedule[i][0];
    //console.log("두 수 비교", a_meeting_end, b_meeting_start);
    if (a_meeting_end <= b_meeting_start) {
      prev.push(cur);
      a_meeting_end = schedule[i][1];
    }
  }
  return prev;
}, []);

console.log(ans.length);
