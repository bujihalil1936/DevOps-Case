
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack

helm upgrade --reuse-values -f alert-rules.yaml prometheus  prometheus-community/kube-prometheus-stack -n monitoring
