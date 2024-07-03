class RobotBatteryManager:
    def __init__(self, total_battery=100):
        self.total_battery = total_battery
        self.current_battery = total_battery

    def use_battery(self, usage):
        self.current_battery -= usage
        self.check_battery()

    def serve(self, serve_usage):
        self.use_battery(serve_usage*1.2)

    def collect(self, collect_usage):
        self.use_battery(collect_usage*1.3)

    def check_battery(self):
        if self.current_battery <= 10:
            print("배터리가 10%이하입니다. 모든 활동을 중단하고 지금 즉시 배터리를 충전합니다")
            
        elif self.current_battery <= 30:
            print("배터리가 30%이하입니다. 로봇의 배터리를 충전해주세요")

    def charge_battery(self):
        self.current_battery = self.total_battery
        print(f"배터리가 {self.current_battery}%로 완충되었습니다.")
