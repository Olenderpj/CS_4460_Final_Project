from zmqRemoteApi.clients.python.zmqRemoteApi import RemoteAPIClient
from dr20 import *


def main():
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    startSimulationEnv(sim)

    robot = dr20(sim, "/dr20")
    robot.randomlyExploreForSetTime(360)

    sleep(2)
    sim.stopSimulation()


if __name__ == "__main__":
    main()
