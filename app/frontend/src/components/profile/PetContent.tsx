import { useRef, useState } from "react"
import Modal, { type TModalHandle } from "../ui/Modal"
import ContentLayout from "./ContentLayout"
import PetCard from "./PetCard"
import { INPUT_BASE } from "@/constants/form"
import { ErrorText, Label } from "../form"
import { PET_SPECIES } from "@/constants/pet"
import { useForm } from "react-hook-form"

type TPetForm = {
  name: string
  species: string
  breed: string
  age: number
  healthCondition?: string
  preferences?: string
}

const PetContent = () => {
  const {
    register,
    watch,
    handleSubmit,
    formState: { errors },
  } = useForm<TPetForm>()
  const selectedSpecies = watch("species")

  const petModalRef = useRef<TModalHandle>(null)
  const [selectedPet, setSelectedPet] = useState<number>()

  return (
    <>
      <ContentLayout
        title="Pet(s) Owned"
        action={{
          label: "+ Add Pet",
          onClick: () => petModalRef.current?.openModal(),
        }}
        children={
          <>
            <PetCard
              pet={{
                id: 0,
                name: "Happy",
                species: "Dog",
                breed: "Labrador Retriever",
                age: 2,
                health: "Healthy",
                preferences:
                  "Prefers beef over anything else, does not like medicine, does not like needles, very scared of the vet",
              }}
              onEdit={(id: number) => console.log("Editing pet: ", id)}
              onDelete={(id: number) => console.log("Deleting pet: ", id)}
            />
            <PetCard
              pet={{
                id: 0,
                name: "Milk",
                species: "Cat",
                breed: "Persian",
                age: 5,
                health: "Healthy",
                preferences: "Very friendly, does not mind being touches, bla bla bla bla bla",
              }}
              onEdit={(id: number) => console.log("Editing pet: ", id)}
              onDelete={(id: number) => console.log("Deleting pet: ", id)}
            />
          </>
        }
      />
      <Modal
        ref={petModalRef}
        header={`${selectedPet ? "Edit" : "Add"} Pet`}
        actionButtons={[
          {
            label: "Cancel",
            onClick: () => petModalRef.current?.closeModal(),
            variant: "secondary",
          },
          {
            label: selectedPet ? "Save" : "Add",
            onClick: () => {
              petModalRef.current?.closeModal()
              console.log(selectedPet ? "Saving service..." : "Adding service...")
            },
          },
        ]}
      >
        <form
          onSubmit={handleSubmit((data) => console.log(data))}
          className="max-w-[620px] w-full grid grid-cols-1 md:grid-cols-2 gap-6"
        >
          <div className="col-span-1">
            <Label htmlFor="name" text="Pet Name" />
            <input
              id="name"
              type="text"
              className={INPUT_BASE}
              aria-invalid={!!errors.name}
              {...register("name", { required: "Pet name is required" })}
            />
            <ErrorText error={errors.name} />
          </div>

          <div className="col-span-1">
            <Label htmlFor="species" text="Species" />
            <select
              id="species"
              className={INPUT_BASE}
              aria-invalid={!!errors.species}
              {...register("species", { required: "Species is required" })}
            >
              <option value="" disabled>
                {" "}
                Select…
              </option>
              {PET_SPECIES.map((species) => (
                <option key={species.value} value={species.value}>
                  {species.label}
                </option>
              ))}
            </select>
            <ErrorText error={errors.species} />
          </div>

          <div className="col-span-1">
            <Label htmlFor="breed" text="Breed" />
            <select
              id="breed"
              className={INPUT_BASE}
              aria-invalid={!!errors.breed}
              disabled={!selectedSpecies}
              {...register("breed", { required: "Breed is required" })}
            >
              <option value="" disabled>
                {" "}
                Select…
              </option>
              {PET_SPECIES.find((species) => species.value === selectedSpecies)?.breeds.map(
                (breed) => (
                  <option key={breed.value} value={breed.value}>
                    {breed.label}
                  </option>
                ),
              )}
            </select>
            <ErrorText error={errors.breed} />
          </div>

          <div className="col-span-1">
            <Label htmlFor="age" text="Age" />
            <input
              id="age"
              type="number"
              className={INPUT_BASE}
              aria-invalid={!!errors.age}
              {...register("age", {
                required: "Age is required",
              })}
            />
            <ErrorText error={errors.age} />
          </div>

          <div className="col-span-1 md:col-span-2">
            <Label htmlFor="healthCondition" text="Health Condition" />
            <textarea
              id="healthCondition"
              className={INPUT_BASE}
              aria-invalid={!!errors.healthCondition}
              placeholder="Any health conditions, allergies, or special requirements..."
              {...register("healthCondition")}
            />
            <ErrorText error={errors.healthCondition} />
          </div>

          <div className="col-span-1 md:col-span-2">
            <Label htmlFor="preferences" text="Preferences" />
            <textarea
              id="preferences"
              className={INPUT_BASE}
              aria-invalid={!!errors.preferences}
              placeholder="Any special care instructions, behavioural notes, or preferences..."
              {...register("preferences")}
            />
            <ErrorText error={errors.preferences} />
          </div>
        </form>
      </Modal>
    </>
  )
}

export default PetContent
