sh scripts/run_connection_deployment.sh
sh scripts/run_persons_deployment.sh
sh scripts/run_frontend_deployment.sh
sh scripts/run_locations_deployment.sh

# Apply deployments
kubectl apply -f deployment/

kubectl get pods