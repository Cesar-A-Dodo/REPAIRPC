from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_PASTA_TERMICA = "TPT", "Trocar pasta termica"
    TROCAR_PLACA_MAE = "TPM", "Trocar placa mãe"
    TROCAR_PlACA_DE_VIDEO = "TPV", "Trocar placa de video"
    TROCAR_FONTE = "TFT", "Trocar fonte"
    TROCAR_MEMORIAS = "TMM", "Trocar memorias"
    TROCAR_PROCESSADOR = "TPC", "Trocar processador"
    TROCAR_ARMAZENAMENTO = "TAM", "Trocar HDD/SSD"
    