from flask import Flask, redirect, render_template, jsonify,request, url_for
import subprocess
from charging import RobotBatteryManager
import serving
import collecting
import turtle
import heapq

app = Flask(__name__)

# Create an instance of RobotBatteryManager
robot_battery_manager = RobotBatteryManager()



@app.route("/")
def index():
    return render_template("index4.2.html")
 
@app.route("/show_turtle_page1")
def show_turtle_page1():
    try:
        output = subprocess.check_output(["python", "serving.py"], stderr=subprocess.STDOUT)
        output_str = output.decode('utf-8').strip()  # Decode bytes to string and strip whitespace
        serve_usage = int(output_str)  # Assuming the output is a single integer value
        robot_battery_manager.serve(serve_usage)  # Update battery manager with serve usage
        message = f"서빙 이동거리: {serve_usage}m , 배터리 사용량 : {serve_usage*1.2}%"
        print(message)
    except subprocess.CalledProcessError as e:
        message = f"Error: {e.output.decode('utf-8').strip()}"
        print(message)
    
    return jsonify({"message": message})


@app.route("/show_turtle_pageA")
def show_turtle_pageA():
    serving.show()
    return redirect(url_for("index")) 

@app.route("/show_turtle_page2")
def show_turtle_page2():
    try:
        output = subprocess.check_output(["python", "collecting.py"], stderr=subprocess.STDOUT)
        output_str = output.decode('utf-8').strip()  # Decode bytes to string and strip whitespace
        collect_usage = int(output_str)  # Assuming the output is a single integer value
        robot_battery_manager.collect(collect_usage)  # Update battery manager with collect usage
        message = f"그릇 회수 이동거리: {collect_usage}m , 배터리 사용량 : {collect_usage*1.3}%"
        print(message)
    except subprocess.CalledProcessError as e:
        message = f"Error: {e.output.decode('utf-8').strip()}"
        print(message)
    
    return jsonify({"message": message})


@app.route("/show_turtle_pageB")
def show_turtle_pageB():
    collecting.show()
    return redirect(url_for("index")) 



@app.route("/charge_robot")
def charge_robot():
    robot_battery_manager.charge_battery()  # Call the charge battery method
    message = f"Battery charged to {robot_battery_manager.current_battery}%"
    print(message)
    return jsonify({"message": message})




@app.route("/battery_status")
def battery_status():
    return jsonify({"battery": robot_battery_manager.current_battery})




@app.route("/check_battery_status")
def check_battery_status():
    status = 'normal'  # 기본적으로 정상 상태로 설정
    status_message = "배터리 상태가 정상입니다"  # 기본 메시지
    
    if robot_battery_manager.current_battery <= 10:
        robot_battery_manager.charge_battery()  # 배터리 재충전
        status_message = "배터리가 10%이하입니다. 모든 활동을 중단하고 지금 즉시 배터리를 충전합니다"
        status = 'low'
    elif robot_battery_manager.current_battery <= 30:
        status_message = "배터리가 30%이하입니다. 로봇의 배터리를 충전해주세요"
        status = 'medium'
    # else:
    #     status_message = "배터리 상태가 정상입니다"
    
    return jsonify({"status": status, "message": status_message})



if __name__ == "__main__":
    app.run(debug=True)
