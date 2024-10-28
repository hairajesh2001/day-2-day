usefull commands for kubernetes

 kubectl get pods -o custom-columns="POD:metadata.name,NODE:spec.nodeName" | tail -n +2 | while read pod node; do
 echo -n "$pod $node "
 kubectl get node "$node" -o jsonpath="{.metadata.labels.topology\.kubernetes\.io/zone}"
 echo ""
done

2) List of nodes and how many pods running on them:
kubectl get po -o json --all-namespaces | \
 jq '.items | group_by(.spec.nodeName) | map({"nodeName": .[0].spec.nodeName, "count": length}) | sort_by(.count)'

3) List pods using most of RAM and CPU:
For CPU:
kubectl top pods -A | sort --reverse --key 3 --numeric

For RAM:
kubectl top pods -A | sort --reverse --key 4 --numeric

4) Getting pods that are continuously restarting (sorting them):
kubectl get pods --all-namespaces -o json | jq -r '.items | sort_by(.status.containerStatuses[0].restartCount) | reverse[] | [.metadata.namespace, .metadata.name, .status.containerStatuses[0].restartCount] | @tsv' | column -t

5) Quickly check the pod limits:
kubectl get pods -o=custom-columns='NAME:spec.containers[*].name,MEMREQ:spec.containers[*].resources.requests.memory,MEMLIM:spec.containers[*].resources.limits.memory,CPUREQ:spec.containers[*].resources.requests.cpu,CPULIM:spec.containers[*].resources.limits.cpu'

6) Get all private IPs of nodes:
kubectl get nodes -o json | \
 jq -r '.items[].status.addresses[]? | select (.type == "InternalIP") | .address' | \
 paste -sd "\n" -

7) Checking logs:
Read logs with human readable timestamp:
kubectl logs -f my-pod --timestamps

Check 100 logs:
kubectl logs -f my-pod --tail=100

8) Check for events across all namespaces and filter for any errors,
kubectl get events --all-namespaces --field-selector type=Warning -o wide
or 
kubectl get events --all-namespaces --field-selector type!=Normal -o wide
