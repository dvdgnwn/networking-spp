# Copyright 2017 NTT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


SPP_ROOT = "/spp/openstack/"

# configuration of each agent
# /spp/openstack/configuration/<host>
SPP_PREFIX_CONF = SPP_ROOT + "configuration/"
SPP_KEY_CONF = SPP_PREFIX_CONF + "{host}"

# manage vhost usage
# /spp/openstack/vhost/<host>/<phys>/<vhost_id>
SPP_PREFIX_VHOST = SPP_ROOT + "vhost/"
SPP_PREFIX_VHOST_HOST = SPP_PREFIX_VHOST + "{host}/"
SPP_PREFIX_VHOST_HOST_PHYS = SPP_PREFIX_VHOST_HOST + "{phys}/"
SPP_KEY_VHOST = SPP_PREFIX_VHOST_HOST_PHYS + "{vhost_id}"

# to indicate plug done
# /spp/openstack/port_status/<host>/<port id>
SPP_PREFIX_PORT_STATUS = SPP_ROOT + "port_status/"
SPP_PREFIX_PORT_STATUS_HOST = SPP_PREFIX_PORT_STATUS + "{host}/"
SPP_KEY_PORT_STATUS = SPP_PREFIX_PORT_STATUS_HOST + "{port_id}"

# port info for plug
# /spp/openstack/bind_port/<host>/<port id>
SPP_PREFIX_BIND_PORT = SPP_ROOT + "bind_port/"
SPP_PREFIX_PORT_BIND_PORT_HOST = SPP_PREFIX_BIND_PORT + "{host}/"
SPP_KEY_BIND_PORT = SPP_PREFIX_PORT_BIND_PORT_HOST + "{port_id}"

# plug/unplug port
# /spp/openstack/action/<host>/<port id>
SPP_PREFIX_ACTION = SPP_ROOT + "action/"
SPP_PREFIX_ACTION_HOST = SPP_PREFIX_ACTION + "{host}/"
SPP_KEY_ACTION = SPP_PREFIX_ACTION_HOST + "{port_id}"

# manage mirror usage
# /spp/openstack/mirror/<host>/<mirror_id>
SPP_PREFIX_MIRROR = SPP_ROOT + "mirror/"
SPP_PREFIX_MIRROR_HOST = SPP_PREFIX_MIRROR + "{host}/"
SPP_KEY_MIRROR = SPP_PREFIX_MIRROR_HOST + "{mirror_id}"

# to indicate tap plug done
# /spp/openstack/tap_status/<host>/<tap_flow_id>
SPP_PREFIX_TAP_STATUS = SPP_ROOT + "tap_status/"
SPP_PREFIX_TAP_STATUS_HOST = SPP_PREFIX_TAP_STATUS + "{host}/"
SPP_KEY_TAP_STATUS = SPP_PREFIX_TAP_STATUS_HOST + "{tap_flow_id}"

# info for tap plug
# /spp/openstack/tap_info/<host>/<tap_flow_id>
SPP_PREFIX_TAP_INFO = SPP_ROOT + "tap_info/"
SPP_PREFIX_TAP_INFO_HOST = SPP_PREFIX_TAP_INFO + "{host}/"
SPP_KEY_TAP_INFO = SPP_PREFIX_TAP_INFO_HOST + "{tap_flow_id}"

# plug/unplug tap
# /spp/openstack/tap_action/<host>/<tap_flow_id>
SPP_PREFIX_TAP_ACTION = SPP_ROOT + "tap_action/"
SPP_PREFIX_TAP_ACTION_HOST = SPP_PREFIX_TAP_ACTION + "{host}/"
SPP_KEY_TAP_ACTION = SPP_PREFIX_TAP_ACTION_HOST + "{tap_flow_id}"


def configuration_key(host):
    return SPP_KEY_CONF.format(**locals())


def vhost_phys_prefix(host, phys):
    return SPP_PREFIX_VHOST_HOST_PHYS.format(**locals())


def vhost_key(host, phys, vhost_id):
    return SPP_KEY_VHOST.format(**locals())


def port_status_prefix():
    return SPP_PREFIX_PORT_STATUS


def port_status_key(host, port_id):
    return SPP_KEY_PORT_STATUS.format(**locals())


def bind_port_key(host, port_id):
    return SPP_KEY_BIND_PORT.format(**locals())


def action_host_prefix(host):
    return SPP_PREFIX_ACTION_HOST.format(**locals())


def action_key(host, port_id):
    return SPP_KEY_ACTION.format(**locals())


def mirror_prefix(host):
    return SPP_PREFIX_MIRROR_HOST.format(**locals())


def mirror_key(host, mirror_id):
    return SPP_KEY_MIRROR.format(**locals())


def tap_status_key(host, tap_flow_id):
    return SPP_KEY_TAP_STATUS.format(**locals())


def tap_info_host_prefix(host):
    return SPP_PREFIX_TAP_INFO_HOST.format(**locals())


def tap_info_key(host, tap_flow_id):
    return SPP_KEY_TAP_INFO.format(**locals())


def tap_action_host_prefix(host):
    return SPP_PREFIX_TAP_ACTION_HOST.format(**locals())


def tap_action_key(host, tap_flow_id):
    return SPP_KEY_TAP_ACTION.format(**locals())
