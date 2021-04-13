
local_v4_cluster:
	kind create cluster --name=kind-v4 --config=kind-v4.yaml

local_v6_cluster:
	kind create cluster --name=kind-v6 --config=kind-v6.yaml
