class numerical {
  constructor(num, symbol, count, prev_num, curr_num, highlight, prev, curr_op) {
      this.num = num;
      this.symbol = symbol;
      this.count = count;
      this.prev_num = prev_num;
      this.curr_num = curr_num;
      this.highlight = highlight;
      this.prev = prev;
      this.curr_op = curr_op;
  }
}

var problem_string = new numerical("", "", 0, "", "", "", "", "");
var solution = 0;
var temp = 0;
var limit = 0;

function getValue(input) {
  if(problem_string.highlight != ""){
    ResetColor();
  }
  if ((limit != "1") || (input != ".")) {
    problem_string.num += input;
    if (input == ".") {
      limit = "1";
    }
  }
  document.getElementById("Answer").innerHTML = problem_string.num;
}

function symbol(input){ 
  if((problem_string.highlight != input)&&(problem_string.highlight != "")){
    document.getElementById(problem_string.highlight).style.backgroundColor='aquamarine';
  }

  problem_string.highlight = input;
  document.getElementById(input).style.backgroundColor='Yellow';
  problem_string.count = problem_string.count + 1;
  problem_string.symbol = input;
  if(problem_string.prev == ""){
      problem_string.prev = problem_string.symbol;
  }
  if (problem_string.prev_num == "") {
      problem_string.prev_num = problem_string.num;
  }
  else if(problem_string.curr_num == ""){
      problem_string.curr_num = problem_string.num;
  }
  else{
      problem_string.curr_num = problem_string.num;
  }

  temp = problem_string.symbol;
  problem_string.symbol = problem_string.prev; 
  problem_string.prev = temp;
  if((problem_string.prev_num != "") && (problem_string.curr_num != "") && (problem_string.count >= 2)){  
      problem_string.curr_op = problem_string.symbol;
      solve(problem_string.count);
      problem_string.curr_num = problem_string.num;
  }

  problem_string.num = "";
  limit = 0;
  problem_string.curr_op = input;
}

function allClear() {
  problem_string.num = "";
  problem_string.prev_num = "";
  problem_string.curr_num = "";
  problem_string.count = 0;
  problem_string.prev = "";
  problem_string.symbol = "";
  problem_string.curr_op = "";
  document.getElementById("Answer").innerHTML = 0;
  document.getElementById('+').style.backgroundColor='aquamarine';
  document.getElementById('-').style.backgroundColor='aquamarine';
  document.getElementById('*').style.backgroundColor='aquamarine';
  document.getElementById('÷').style.backgroundColor='aquamarine';
}

function solve(input) {
  if(input == 0){
      ResetColor();
  }
  if(problem_string.num != ""){    
      problem_string.curr_num = problem_string.num;
  }
  if (problem_string.curr_op == "÷") {
      solution = (parseFloat(problem_string.prev_num)) / (parseFloat(problem_string.curr_num))
  }
  if (problem_string.curr_op == "-") {
      solution = (parseFloat(problem_string.prev_num)) - (parseFloat(problem_string.curr_num))
  }
  if (problem_string.curr_op == "+") {
      solution = (parseFloat(problem_string.prev_num)) + (parseFloat(problem_string.curr_num))
  }
  if (problem_string.curr_op == "*") {
      solution = (parseFloat(problem_string.prev_num)) * (parseFloat(problem_string.curr_num))
  }
  document.getElementById("Answer").innerHTML = solution;
  problem_string.prev_num = solution;
  problem_string.num = "";
}

function ResetColor(){
  document.getElementById(problem_string.highlight).style.backgroundColor='aquamarine';
}