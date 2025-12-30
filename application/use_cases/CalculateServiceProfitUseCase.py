class CalculateServiceProfitUseCase:
    def execute(self, service_id: str) -> float:
        service = service_repository.get_service(service_id)

        policy = policy_provider.get_active_policy()
        
        snapshot = service.calculate_profit(policy)
        service.finalize()
        
        service_repository.save_service(service)

        return snapshot
