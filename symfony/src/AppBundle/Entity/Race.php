<?php

namespace AppBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass="AppBundle\Repository\RaceRepository")
 * @ORM\Table(name="races")
 */
class Race
{

    // Fields {{{

    /**
     * @ORM\Id
     * @ORM\Column(type="integer")
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $name;

    /**
     * @ORM\Column(name="deleted_at", type="datetime", nullable=true)
     */
    private $deletedAt;

    // }}}

    // Relations {{{

    /**
     * @ORM\ManyToOne(targetEntity="Specie")
     */
    private $specie;

    // }}}

    // Custom methods {{{
    // }}}

    // Automatic created methods {{{

    /**
     * Get id
     *
     * @return integer
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set name
     *
     * @param string $name
     *
     * @return Race
     */
    public function setName($name)
    {
        $this->name = $name;

        return $this;
    }

    /**
     * Get name
     *
     * @return string
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * Set deletedAt
     *
     * @param \DateTime $deletedAt
     *
     * @return Race
     */
    public function setDeletedAt($deletedAt)
    {
        $this->deletedAt = $deletedAt;

        return $this;
    }

    /**
     * Get deletedAt
     *
     * @return \DateTime
     */
    public function getDeletedAt()
    {
        return $this->deletedAt;
    }

    /**
     * Set specie
     *
     * @param \AppBundle\Entity\Specie $specie
     *
     * @return Race
     */
    public function setSpecie(\AppBundle\Entity\Specie $specie = null)
    {
        $this->specie = $specie;

        return $this;
    }

    /**
     * Get specie
     *
     * @return \AppBundle\Entity\Specie
     */
    public function getSpecie()
    {
        return $this->specie;
    }

    // }}}

}
