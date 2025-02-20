package dsdv25;

import inet.common.scenario.ScenarioManager;
import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.networklayer.ipv4.RoutingTableRecorder;
import inet.node.dsdv.DsdvRouter;
import inet.physicallayer.wireless.unitdisk.UnitDiskRadioMedium;

network dsdv25AdhocHighMobilityNetwork
{
    parameters:
        @display("bgb=700,700");
    submodules:
        radioMedium: UnitDiskRadioMedium {
            parameters:
                @display("p=100,100;is=s");
        }
        configurator: Ipv4NetworkConfigurator {
            parameters:
                addDefaultRoutes = false;
                addStaticRoutes = false;
                addSubnetRoutes = false;
                config = xml("<config> \
                    <interface hosts='host[*]' address='10.x.x.x' netmask='255.255.255.0'/> \
                </config>");
                @display("p=100,200;is=s");
        }
        routingTableRecorder: RoutingTableRecorder {
            parameters:
                @display("p=100,300;is=s");
        }
        scenarioManager: ScenarioManager {
            parameters:
                script = default(xml("<scenario/>"));
                @display("p=100,400;is=s");
        }
        //host[25]: AodvRouter {
        host[25]: DsdvRouter {
            parameters:
                @display("i=device/pocketpc_s;r=,,#707070");
        }
    connections allowunconnected:
}
