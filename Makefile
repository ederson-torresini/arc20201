all: init plan apply show

file = "gcp.tfvars"

init:
	terraform init

plan: init
	terraform plan -var-file=$(file)

apply: plan
	terraform apply -var-file=$(file)

show:
	terraform show

clean:
	terraform destroy -var-file=$(file)
